# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1722",
)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE crm")

print("All done!")