PRAGMA foreign_keys = ON;

-- CREATE DATABASE IF NOT EXISTS recipe_book;
-- USE recipe_book;


CREATE TABLE IF NOT EXISTS Recipes (
    RecipeID INTEGER DEFAULT 1 PRIMARY KEY AUTOINCREMENT NOT NULL,
    Title VARCHAR(100) NOT NULL,
    Created_By VARCHAR(100),
    Description TEXT,
    PreparationTime INT UNSIGNED,
    CookingTime INT UNSIGNED,
    Servings INT UNSIGNED,
    Instructions TEXT,
    EquipmentID INT NOT NULL,
    IngredientID INT NOT NULL,
    FOREIGN KEY (EquipmentID) REFERENCES Equipment (EquipmentID) ON DELETE CASCADE,
    FOREIGN KEY (IngredientID) REFERENCES Ingredients (IngredientID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS CuisineCategories (
    CuisineCategoryID INTEGER PRIMARY AUTOINCREMENT  KEY NOT NULL,
    CategoryName VARCHAR(100) NOT NULL,
    RecipeID INT NOT NULL,
    FOREIGN KEY (RecipeID) REFERENCES Recipes (RecipeID) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS DietaryCategories (
    DietaryCategoryID INTEGER PRIMARY AUTOINCREMENT  KEY NOT NULL,
    DietaryName VARCHAR(100) NOT NULL,
    RecipeID INT NOT NULL,
    FOREIGN KEY (RecipeID) REFERENCES Recipes (RecipeID) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Equipment (
    EquipmentID INTEGER PRIMARY AUTOINCREMENT  KEY NOT NULL,
    EquipmentName VARCHAR(100) NOT NULL,
    UseDescription VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS Ingredients (
    IngredientID INTEGER PRIMARY AUTOINCREMENT  KEY NOT NULL,
    Name VARCHAR(100) NOT NULL,
    IsAllergen BOOLEAN DEFAULT FALSE,
    DietaryRestrictions VARCHAR(255)
);