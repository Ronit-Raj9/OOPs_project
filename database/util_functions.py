import mysql.connector
import csv
from mysql.connector import Error

def is_id_present(vehicle_id):
    """
    Returns true if an ID exists in the table, false otherwise.
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
            cursor = conn.cursor()
            select_query = "SELECT * FROM vehicle_details WHERE SERIAL_NO = {}".format(vehicle_id)
            
            cursor.execute(select_query)
            row = cursor.fetchone()
            
            return bool(row)
        
    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()            

def get_row_by_vehicle_no(vehicle_no):
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
            cursor = conn.cursor()
            select_query = "SELECT * FROM vehicle_details WHERE VEHICLE_NO = \"{}\"".format(vehicle_no)
            
            cursor.execute(select_query)
            row = cursor.fetchone()
            
            return row
        
    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()