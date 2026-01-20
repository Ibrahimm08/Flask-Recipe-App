PRAGMA foreign_keys = ON;



CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Description TEXT,
    TechnicalDetails TEXT,
    Brand VARCHAR(50),
    Catagory TEXT,
    Stock INT,
    RatingID INT NOT NULL,
    SupplierID INT NOT NULL,
    FOREIGN KEY (RatingID) REFERENCES Rating (id) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Supplier (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Supplier (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactInfo TEXT,
    IsAvailable BOOL
);

CREATE TABLE IF NOT EXISTS Catagory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    ProductID INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products (id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Rating(
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Comment TEXT NOT NULL,
    Rating INT NOT NULL,
    ReviewDate CURRENT_DATE,
    ProductID INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products (id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    CatagoryID INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products (id) ON DELETE CASCADE
    FOREIGN KEY (CatagoryID) REFERENCES Catagory (id) ON DELETE CASCADE
);