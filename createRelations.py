#!/usr/bin/python

import psycopg2
from config import config

def create_relations():
    """ create relations for our tables in the PostgreSQL database"""
    commands = (
        """ CREATE TABLE EmployeeHandles (
                TicketId INT NOT NULL,
                EmployeeID INT NOT NULL,
                PRIMARY KEY (TicketId, EmployeeID),
                FOREIGN KEY (TicketId) REFERENCES SupportTickets (TicketId) on DELETE CASCADE,
                FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeId) on DELETE CASCADE
            )
        """,
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
    create_relations()