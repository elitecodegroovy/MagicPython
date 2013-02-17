__author__ = 'JohnLiu'
import MySQLdb

# Open database connection
db = MySQLdb.connect("127.0.0.1","root","elite","pythondb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

creationSQL = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

#create a table
cursor.execute(creationSQL)
# Prepare SQL query to INSERT a record into the database.
insertedSQL = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # Execute the SQL command
    cursor.execute(insertedSQL)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

#disconnect from server
db.close()