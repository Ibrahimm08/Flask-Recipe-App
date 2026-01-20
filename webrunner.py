from flask import Flask, request, render_template, jsonify, redirect, session
import mysql.connector
import sqlite3

app = Flask(__name__)
app.secret_key = "asdfawf"

db = "database.db"

try: 
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor() 
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print("Error:", err)

@app.route("/") 
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    ingredientID = session.get("ing", {})
    equipmentID = session.get("equ", {})
    
    equipment = ""
    ingredient = ""
    
    if equipmentID:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        sql = """ 
            SELECT EquipmentName FROM EQUIPMENT WHERE EquipmentID = ?
        """
        values = equipmentID
        
        equipment = cursor.execute(sql, values).fetchone()[0]
                
        conn.commit()
        cursor.close()
        conn.close()
    
    if ingredientID:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        sql = """ 
            SELECT Name FROM INGREDIENTS WHERE IngredientID = ?
        """
        values = ingredientID
        
        ingredient = cursor.execute(sql, values).fetchone()[0]
             
        conn.commit()
        cursor.close()
        conn.close()
        
    if request.method == 'POST':
        session["recipeSession"] = request.form.to_dict()

        if request.form.get("addIngredient") == "addIng":
            return redirect("addIngredient")
        elif request.form.get("addEquipment") == "addEqu":
            return redirect("addEquipment")
        
        title = request.form['title']
        created_by = request.form['createdBy']
        description = request.form['description']
        prep_time = request.form['preparationTime']
        cook_time = request.form['cookingTime']
        servings = request.form['servings']
        instructions = request.form['instructions']
           
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        sql = """
            INSERT INTO Recipes 
            (Title, Created_By, Description, PreparationTime, CookingTime, Servings, Instructions, EquipmentID, IngredientID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (title, created_by, description, prep_time, cook_time, servings, instructions, equipmentID, ingredientID)

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()
        
    saved = session.get("recipeSession", {})
    print(saved)

    return render_template('index.html', saved=saved, ingredient=ingredient, equipment=equipment ) 


@app.route("/addEquipment", methods=['GET', 'POST'])
def get_equipment():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    equipment =  cursor.execute("SELECT * FROM EQUIPMENT").fetchall()
    
    for row in equipment:
        print(row)
    cursor.close()
    conn.close()
    
    if request.method == 'POST':
        session["equ"] = request.form["option"]
        print(request.form["option"])
        return redirect("add_recipe")
    return render_template("addEquipment.html", equipment = equipment)

@app.route("/addIngredient", methods=['GET', 'POST'])
def get_ingredient():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    ingredients =  cursor.execute("SELECT * FROM INGREDIENTS").fetchall()
    for row in ingredients:
        print(row)
    cursor.close()
    conn.close()
    
    if request.method == 'POST':
        session["ing"] = request.form["option"]
        print(request.form["option"])
        return redirect("add_recipe")
    return render_template("addIngredient.html", ingredients = ingredients)
   



if __name__ == '__main__':
    app.run(debug=True)
