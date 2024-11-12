-- DateDimension
CREATE TABLE DateDimension (
    DateID INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Month INT,
    Day INT,
    Quarter INT
);

-- ProductDimension
CREATE TABLE ProductDimension (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    ProductCategory VARCHAR(255),
    ProductSubCategory VARCHAR(255),
    ProductPrice DECIMAL(10,2)
);

-- CustomerDimension
CREATE TABLE CustomerDimension (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerEmail VARCHAR(255),
    CustomerSegment VARCHAR(50)
);

-- SupplierDimension
CREATE TABLE SupplierDimension (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255),
    SupplierLocation VARCHAR(255),
    SupplierContact VARCHAR(50)
);

-- ShipperDimension
CREATE TABLE ShipperDimension (
    ShipperID INT PRIMARY KEY,
    ShipperName VARCHAR(255),
    ShippingMethod VARCHAR(50)
);
