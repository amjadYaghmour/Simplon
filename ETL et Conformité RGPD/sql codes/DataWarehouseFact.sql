-- SalesFact
CREATE TABLE SalesFact (
    SalesID INT IDENTITY(1,1) PRIMARY KEY,
    DateID INT,
    ProductID INT,
    CustomerID INT,
    SupplierID INT,
    ShipperID INT,
    QuantitySold INT,
    TotalAmount DECIMAL(10,2),
    DiscountAmount DECIMAL(10,2),
    NetAmount DECIMAL(10,2),
    
    -- Foreign Key Constraints
    FOREIGN KEY (DateID) REFERENCES DateDimension(DateID),
    FOREIGN KEY (ProductID) REFERENCES ProductDimension(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES CustomerDimension(CustomerID),
    FOREIGN KEY (SupplierID) REFERENCES SupplierDimension(SupplierID),
    FOREIGN KEY (ShipperID) REFERENCES ShipperDimension(ShipperID)
);


-- InventoryFact
CREATE TABLE InventoryFact (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    DateID INT,
    ProductID INT,
    SupplierID INT,
    StockReceived INT,
    StockSold INT,
    StockOnHand INT,
    FOREIGN KEY (DateID) REFERENCES DateDimension(DateID),
    FOREIGN KEY (ProductID) REFERENCES ProductDimension(ProductID),
    FOREIGN KEY (SupplierID) REFERENCES SupplierDimension(SupplierID)
);
