import random 
import psycopg2
from config import config

employees_first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
employees_last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

ticketBank1 = ['a question' , 'a problem' , 'an issue' , 'a complaint' ,'a request' ] 
ticketBank2 = ['a product' , 'my shipment' , 'my package' , 'shipping' , 'price' , 'an error'  ]

customers_first_names=[]
customers_last_names=[]

#This list contains random customerID numbers without repetition shhuffled, print to see it
accounts_cid = random.sample(list(range(1,101)), k=100)
fake_Passwords=[]

#This is a dictionary to store each email with it's associated customerID
customer_id_email={}

fake_companies=[]

filename1='firstNames.txt'
filename2='lastNames.txt'
filename3='fakePasswords.txt'
filename4='fakeCompanies.txt'

with open (filename1) as fin:
    for line in fin:
        customers_first_names.append(line.strip())


with open (filename2) as fin:
    for line in fin:
        customers_last_names.append(line.strip())

with open (filename3) as fin:
    for line in fin:
        fake_Passwords.append(line.strip())

with open (filename4) as fin:
    for line in fin:
        fake_companies.append(line.strip())



def insert_employee(Fname, Lname):
    sql = """INSERT INTO employees(FName, LName)
             VALUES(%s, %s) RETURNING EmployeeId;"""
    conn = None
    EmployeeId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Fname,Lname))
        # get the generated id back
        EmployeeId = cur.fetchone()[0]
        print("The EmployeeId is: "+f'{EmployeeId}')
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return EmployeeId


def insert_customers(Fname, Lname, Phone, Email, Address, City, State, Zip):
    sql = """INSERT INTO customers(Fname, Lname, Phone, Email, Address, City, State, Zip)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING CustomerId;"""
    conn = None
    CustomerId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Fname,Lname,Phone,Email,Address,City,State,Zip))
        # get the generated id back
        CustomerId = cur.fetchone()[0]
        print("The CustomerId is: "+f'{CustomerId}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return CustomerId

    
def insert_tickets(cid,supportmessage,oid,eid,ticketdate):
    sql = """INSERT INTO SupportTickets(CustomerId, SupportMessage , OrderId, EmployeeId, TicketDate)
            VALUES(%s, %s, %s, %s, %s) RETURNING TicketId;"""
    conn = None
    TicketId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (cid,supportmessage,oid,eid,ticketdate))
        # get the generated id back
        TicketId = cur.fetchone()[0]
        print("The TicketId is: "+f'{TicketId}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return TicketId


def insert_orders(cid, orderDate, trackingNo, carrierid):
    sql = """INSERT INTO Orders(CustomerId, OrderDate , TrackingNo, CarrierId)
            VALUES(%s, %s, %s, %s) RETURNING OrderId;"""
    conn = None
    oid = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (cid, orderDate, trackingNo, carrierid))
        # get the generated id back
        oid = cur.fetchone()[0]
        print("The OrderId is: "+f'{oid}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return oid


def insert_accounts(Email, password, CustomerId):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO accounts(Email, password, CustomerId)
            VALUES(%s, %s, %s) RETURNING UserId;"""
    conn = None
    UserId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Email,password,CustomerId))
        # get the generated id back
        UserId = cur.fetchone()[0]
        print("The UserId is: "+f'{UserId}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return UserId


def get_email():
    # """ query data from the customers table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT customerid, email FROM Customers ORDER BY customerid")
        print("The number of customers: ", cur.rowcount,"\n")
        row = cur.fetchone()
 
        while row is not None:
            # print("id: ", row[0])
            # print("email: ", row[0])
            customer_id_email[row[0]]=row[1]
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_suppliers(SupplierName):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO Suppliers(SupplierName)
             VALUES(%s) RETURNING SupplierID;"""
    conn = None
    SupplierID = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (SupplierName,))
        # get the generated id back
        SupplierID = cur.fetchone()[0]
        print("The SupplierID is: "+f'{SupplierID}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return SupplierID



if __name__ == '__main__':
    
    #generates 100 fake employees
    # UNCOMMENT TO INSERT AND CHANGE range to range(100)
    print("The Employees are:","\n")
    for x in range(1):
    
        first_employee = random.choice(employees_first_names)
        last_employee = random.choice(employees_last_names)

        # insert_employee(first_employee, first_employee)
        # print(f'{first_employee} {last_employee}\n')
        # print("#"*50)
        # print(" ")


    #generates 100 fake customers
    # UNCOMMENT TO INSERT AND CHANGE range to range(100)
    print("The Customers are:","\n")
    for x in range(1):
        first_customer = random.choice(customers_first_names)
        last_customer = random.choice(customers_last_names)

        phone_string = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

        emailAt = '@jetastore.com'
        email = f'{first_customer.lower()}{last_customer.lower()}{emailAt}'

        street_num = random.randint(100, 999)
        street = random.choice(street_names)
        city = random.choice(fake_cities)
        state = random.choice(states)
        zip_string = f'{random.randint(10000, 99999)}'
        address = f'{street_num} {street} St.,'
        
        # insert_customers(first_customer, last_customer, phone_string, email, address, city, state, zip_string)
        # print(f'{first_customer}\n{last_customer}\n{phone_string}\n{email}\n{address}\n{city}\n{state}\n{zip_string}\n')
        # print("#"*50)
        # print(" ")

     ##generates fake Orders:
    print("The Orders are","\n")
    for x in range(1):
        cid = random.randint(1,100)
        yr = random.randint(2016,2018)
        mo = random.randint(1,12)
        day = random.randint(1,28)
        orderDate = f'{str(yr)}-{str(mo)}-{str(day)}'
        carrierid = random.randint(1,4)
        trackingNo = random.randint(10000000,99999999)

        # insert_orders(cid,orderDate,trackingNo, carrierid)
        # print ("The order is: ", f'{cid} {yr} {mo} {day} {orderDate} {carrierid} {trackingNo}\n')
        # print("#"*50)
        # print(" ")


    ##generates fake tickets:
    print("The Tickets are:","\n")
    for x in range(1):
        cid = random.randint(1,100)
        oid = random.randint(1,100)
        eid = random.randint(1,100)
        yr = random.randint(2016,2018)
        mo = random.randint(1,12)
        day = random.randint(1,28)
        ticketdate = f'{str(yr)}-{str(mo)}-{str(day)}'
        supportMessage = f'I have {random.choice(ticketBank1)} about {random.choice(ticketBank2)}'

        # insert_tickets(cid,supportMessage,oid,eid,ticketdate)
        # print("The ticket is: ",supportMessage,"\n")
        # print("#"*50)
        # print(" ")
    
    ##generates fake accounts:
    #We run get_email() so we can get the emails
    get_email()
    print(accounts_cid, "\n")
    print("The Accounts are:\n")

    for x in range(1): 
        cid = accounts_cid[x]
        email = customer_id_email.get(cid)
        password = random.choice(fake_Passwords) 

        # insert_accounts(email,password,cid)
        # print(f'{cid} {password} {email}\n')
        # print("#"*50)
        # print(" ")
    

     #generates 100 fake companies
    # UNCOMMENT TO INSERT AND CHANGE range to range(100)
    print("The Companies are:","\n")
    for x in range(100):
        randomCompanies = random.sample(fake_companies, k=100)
        suppliers = random.choice(randomCompanies)

        # insert_suppliers(suppliers)
        print(f'{suppliers}\n')
        print("#"*50)
        print(" ")