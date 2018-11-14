CREATE TABLE Categories
(
  CategoryId SERIAL PRIMARY KEY,
  CategoryName VARCHAR(255) NOT NULL
);

CREATE TABLE Carrier
(
  CarrierId SERIAL PRIMARY KEY,
  CarrierName VARCHAR(255)
  
);

CREATE TABLE Employees
(
  EmployeeId SERIAL PRIMARY KEY,
  FName INT NOT NULL,
  LName INT NOT NULL
);

CREATE TABLE Customers
(
  CustomerId SERIAL PRIMARY KEY,
  FName VARCHAR(255) NOT NULL,
  LName VARCHAR(255) NOT NULL,
  Phone INT NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(255) NOT NULL,
  State VARCHAR(2) NOT NULL,
  Zip INT NOT NULL
);

CREATE TABLE Accounts
(
  username VARCHAR(255) PRIMARY KEY,
  password VARCHAR(255) NOT NULL,
  CustomerId INT NOT NULL
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);

CREATE TABLE Orders
(
  OrderId SERIAL PRIMARY KEY,
  CustomerId INT NOT NULL,
  OrderDate INT NOT NULL,
  TrackingNo INT NOT NULL,
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);

CREATE TABLE Products
(
  ProductId SERIAL PRIMARY KEY,
  ProductName VARCHAR(255),
  Price INT NOT NULL,
  Inventory INT NOT NULL,
  CategoryId INT NOT NULL,
  SupplierId INT NOT NULL
  FOREIGN KEY (CategoryId) REFERENCES Categories(CategoryId)
  FOREIGN KEY (SupplierId) REFERENCES Suppliers(SupplierId)
);

CREATE TABLE Suppliers
(
  SupplierID SERIAL PRIMARY KEY,
  SupplierName VARCHAR(255)
);

CREATE TABLE SupportTickets
(
  TicketId SERIAL PRIMARY KEY,
  CustomerId INT NOT NULL,
  SupportMessage VARCHAR(255),
  OrderId INT,
  EmployeeId INT NOT NULL,
  Date DATE NOT NULL
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
  FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeId)
);

CREATE TABLE OrderDetails
(
  DetailId SERIAL PRIMARY KEY,
  OrderId INT NOT NULL,
  ProductId INT NOT NULL,
  Quantity INT NOT NULL,
  TotalPrice INT
  FOREIGN KEY(OrderId) REFERENCES Orders(OrderId)
  FOREIGN KEY(ProductId) REFERENCES Products(ProductId)
  
);