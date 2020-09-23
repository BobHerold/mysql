import os
import pymysql

# Get username from Cloud9(Gitpod) workspace
# (Modify this variable if running on another environment, like your own pc)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query  
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, reqardless of whether the above was successful
    connection.close()          
