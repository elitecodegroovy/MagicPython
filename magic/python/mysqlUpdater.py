__author__ = 'JohnLiu'
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","elite","elite","pythonDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
deletionSQL =  "DELETE FROM EMPLOYEE WHERE INCOME > '%d'" % (7000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Execute the deletion sql command
    cursor.execute(deletionSQL)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()