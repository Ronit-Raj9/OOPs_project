import csv
import mysql.connector
from mysql.connector import Error

def print_db():
    """
    Displays the whole table.
    """
    try:
        with open('db_details/database_addr.txt', 'r') as file:
            lines = file.readlines()

            host_addr = lines[0].strip()
            port_no = int(lines[1].strip())
        
        conn = mysql.connector.connect(
            host = host_addr,
            port = port_no,
            user = "root",
            passwd = "",
            database = "oops_db"
        )

        if conn.is_connected():
            db = conn.get_server_info()
            print("Connected to database:", db)
            
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `vehicle_details`")
            result = cursor.fetchall()
            
            for row in result:
                print(row)
            
    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection to the database closed successfully.")