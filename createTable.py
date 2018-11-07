#!/usr/bin/python

# [postgresql]
# host=ammandb.postgres.database.azure.com
# database=JetaStore
# user=myadmin@ammandb
# password=forDB2019

import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Employees (
            e_id SERIAL PRIMARY KEY,
            Fname VARCHAR(255) NOT NULL,
            Lname VARCHAR(255) NOT NULL
        )
        """,)
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