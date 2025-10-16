import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="employee_db"
    )
    return conn