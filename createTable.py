#!/usr/bin/python

import psycopg2
from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """ CREATE TABLE Categories (
                CategoryId SERIAL PRIMARY KEY,
                CategoryName VARCHAR(255) NOT NULL
            )
        """,
        """ CREATE TABLE Carriers (
                CarrierId SERIAL PRIMARY KEY,
                CarrierName VARCHAR(255) NOT NULL
            )
        """,
        """ CREATE TABLE Employees (
                EmployeeId SERIAL PRIMARY KEY,
                FName VARCHAR(255) NOT NULL,
                LName VARCHAR(255) NOT NULL
            )
        """,
        """ CREATE TABLE Customers (
                CustomerId SERIAL PRIMARY KEY,
                FName VARCHAR(255) NOT NULL,
                LName VARCHAR(255) NOT NULL,
                Phone VARCHAR(20),
                Email VARCHAR (355) UNIQUE NOT NULL,
                Address VARCHAR(255) NOT NULL,
                City VARCHAR(255) NOT NULL,
                State VARCHAR(2) NOT NULL,
                Zip VARCHAR(10) NOT NULL
            )
        """,
        """ CREATE TABLE Accounts (
                UserId SERIAL PRIMARY KEY,
                Email VARCHAR (355) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                CustomerId INT NOT NULL,
                FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
                FOREIGN KEY (Email) REFERENCES Customers(Email)
            )
        """,
        """ CREATE TABLE Orders (
                OrderId SERIAL PRIMARY KEY,
                CustomerId INT NOT NULL,
                OrderDate DATE NOT NULL,
                TrackingNo INT NOT NULL,
                CarrierId INT NOT NULL,
                FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
                FOREIGN KEY (CarrierId) REFERENCES Carriers(CarrierId)
            )
        """,
         """ CREATE TABLE Suppliers (
                SupplierID SERIAL PRIMARY KEY,
                SupplierName VARCHAR(255)
            )
        """,
        """ CREATE TABLE Products (
                ProductId SERIAL PRIMARY KEY,
                ProductName VARCHAR(255) NOT NULL,
                Price INT NOT NULL,
                Inventory INT NOT NULL,
                CategoryId INT NOT NULL,
                SupplierId INT NOT NULL,
                FOREIGN KEY (CategoryId) REFERENCES Categories(CategoryId),
                FOREIGN KEY (SupplierId) REFERENCES Suppliers(SupplierId) 
            )
        """,
        """ CREATE TABLE SupportTickets (
                TicketId SERIAL PRIMARY KEY,
                CustomerId INT NOT NULL,
                SupportMessage VARCHAR(255),
                OrderId INT,
                EmployeeId INT NOT NULL,
                TicketDate DATE NOT NULL,
                FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
                FOREIGN KEY (OrderId) REFERENCES Orders(OrderId),
                FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeId)
            )
        """,
        """ CREATE TABLE OrderDetails (
                DetailId SERIAL PRIMARY KEY,
                OrderId INT NOT NULL,
                ProductId INT NOT NULL,
                Quantity INT NOT NULL,
                TotalPrice INT NOT NULL,
                FOREIGN KEY(OrderId) REFERENCES Orders(OrderId),
                FOREIGN KEY(ProductId) REFERENCES Products(ProductId)
            )
        """
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
