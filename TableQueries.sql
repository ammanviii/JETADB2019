CREATE TABLE Categories
(
  CategoryId SERIAL PRIMARY KEY,
  CategoryName VARCHAR(255) NOT NULL
);

CREATE TABLE Carriers
(
  CarrierId SERIAL PRIMARY KEY,
  CarrierName VARCHAR(255) NOT NULL

);

CREATE TABLE Employees
(
  EmployeeId SERIAL PRIMARY KEY,
  FName VARCHAR(255) NOT NULL,
  LName VARCHAR(255) NOT NULL
);

CREATE TABLE Customers
(
  CustomerId SERIAL PRIMARY KEY,
  FName VARCHAR(255) NOT NULL,
  LName VARCHAR(255) NOT NULL,
  Phone VARCHAR(20),
  Email VARCHAR (355) UNIQUE NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(255) NOT NULL,
  State VARCHAR(2) NOT NULL,
  Zip VARCHAR(10) NOT NULL
);

CREATE TABLE Accounts
(
  UserId SERIAL PRIMARY KEY,
  Email VARCHAR (355) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  CustomerId INT NOT NULL,
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
  FOREIGN KEY (Email) REFERENCES Customers(Email)
);

CREATE TABLE Orders
(
  OrderId SERIAL PRIMARY KEY,
  CustomerId INT NOT NULL,
  OrderDate DATE NOT NULL,
  TrackingNo INT NOT NULL,
  CarrierId INT NOT NULL,
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
  FOREIGN KEY (CarrierId) REFERENCES Carriers(CarrierId)
);

CREATE TABLE Suppliers
(
  SupplierID SERIAL PRIMARY KEY,
  SupplierName VARCHAR(255)
);

CREATE TABLE Products
(
  ProductId SERIAL PRIMARY KEY,
  ProductName VARCHAR(255) NOT NULL,
  Price DECIMAL NOT NULL,
  Inventory INT NOT NULL,
  CategoryId INT NOT NULL,
  SupplierId INT NOT NULL,
  FOREIGN KEY (CategoryId) REFERENCES Categories(CategoryId),
  FOREIGN KEY (SupplierId) REFERENCES Suppliers(SupplierId)
);

CREATE TABLE SupportTickets
(
  TicketId SERIAL PRIMARY KEY,
  CustomerId INT NOT NULL,
  SupportMessage VARCHAR(255),
  OrderId INT,
  EmployeeId INT NOT NULL,
  TicketDate DATE NOT NULL,
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
  FOREIGN KEY (OrderId) REFERENCES Orders(OrderId),
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeId)
);

CREATE TABLE OrderDetails
(
  DetailId SERIAL PRIMARY KEY,
  OrderId INT NOT NULL,
  ProductId INT NOT NULL,
  Quantity INT NOT NULL,
  TotalPrice DECIMAL NOT NULL,
  FOREIGN KEY(OrderId) REFERENCES Orders(OrderId),
  FOREIGN KEY(ProductId) REFERENCES Products(ProductId)

);