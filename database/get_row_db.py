import mysql.connector
import csv
from mysql.connector import Error
from add_fine_db import add_fine

def get_row(id):
    """
    Returns a dictionary containing the specified ID's details.
    Returns an empty dictionary otherwise.
    Parameters: ID(int)
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

            select_query = "SELECT * FROM vehicle_details WHERE SERIAL_NO = {}".format(id)
            cursor.execute(select_query)
            row = cursor.fetchone()

            if row:
                # print("Vehicle with ID", id, "found")
                return row
    except Error as e:
        print("\nError connecting to database")
        return {}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()