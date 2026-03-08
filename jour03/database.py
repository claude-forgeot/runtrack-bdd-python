import mysql.connector

# Connector Mysql Database
def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root_1234",
        database="store",
        ssl_disabled=True
    )
    return connection