// File was used previously no longer needed

const newFormTarger = document.getElementById("add-form");
var equipmentOptions;
var ingredientOptions;


function showEquipment() {
    newFormTarger.innerHTML = `<form class="add-equipment">
        <h2>Add Equipment</h2>
        
        <label for="option">Choose Equipment</label>
        <select name="option" id="option" onchange="chooseEquipmentOnChange()">
            <option value=""></option>
            <option value="add">---    New Equipment   ---</option>
            ${equipmentOptions}
        </select>

        <button type="button" onclick="addEquipment()">Add</button>
    </form>`;
}

function addEquipment() {
    var select = document.getElementById("option")
    optionSelected = select[select.selectedIndex].value;
    document.getElementById("equipment").value = optionSelected;
}

function chooseEquipmentOnChange() {
    var select = document.getElementById("option")
    optionSelected = select[select.selectedIndex].value;
    if (optionSelected === "add") {
        newFormTarger.innerHTML = `
        <form class="add-equipment">
            <h2>Add Equipment</h2>

            <label for="equipment-name">Equipment name:</label>
            <input type="text" name="equipment-name" maxlength="100" required class="title">

            <label for="description">Use:</label>
            <input type="text" class="description" name="description">
        
            <button type="submit">Add</button>
        </form>
        `;
    }
}




function showIngredient() {
    newFormTarger.innerHTML = `<form class="add-ingredient">
        <h2>Add Ingredient</h2>

        <label for="option">Choose Ingredient</label>
        <select name="option" id="option" onchange="chooseIngredientOnChange()">
            <option value=""></option>
            <option value="add">---    New Ingredient   ---</option>
            ${ingredientOptions}
        </select>
          
        <button type="button" onclick="addIngredient">Add</button>
    </form>`;
}


function addIngredient() {
    var select = document.getElementById("option")
    optionSelected = select[select.selectedIndex].value;
    document.getElementById("ingredient").value = optionSelected;
}


function chooseIngredientOnChange() {
    var select = document.getElementById("option")
    optionSelected = select[select.selectedIndex].value;
    if (optionSelected === "add") {
        newFormTarger.innerHTML = `
        <form class="add-ingredient">
            <h2>Add Ingredient</h2>
            
            <label for="ingredient-name">Ingredient name:</label>
            <input type="text" name="ingredient-name" maxlength="100" required class="title">

             <div>
                <label for="description">Is Allergen?</label>
                <input type="checkbox" class="description" name="description">
            </div>

            <button type="button">Add</button>
        </form>
        `;
    }
}




fetch("/get-equipment")
    .then(response => response.json())
    .then(data => {
        if (data) {
            console.log("fetched Equipment data:", data);
            for (var element in data) {
                equipmentOptions += `
                        <option value="${data[element]["id"]}">${data[element]["name"]}</option>
                    `;
            };
        } else {
            console.log("fetched Equipment data... but nothing was there");
        }
    })
    .catch(err => console.error("Error fetching equipment data:", err));


fetch("/get-ingredient")
    .then(response => response.json())
    .then(data => {
        if (data) {
            console.log("fetched Ingredient data:", data);
            for (var element in data) {
                ingredientOptions += `
                        <option value="${data[element]["id"]}">${data[element]["name"]}</option>
                    `;
            };
        } else {
            console.log("fetched Ingredient data... but nothing was there");
        }
    })
    .catch(err => console.error("Error fetching equipment data:", err));