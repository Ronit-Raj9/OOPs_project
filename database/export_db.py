import csv
import mysql.connector
from mysql.connector import Error

def export_db_to(csv_file_name):
    """
    Exports whole table to the specified CSV file, saved to csv_data folder.
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

            print("Writing to file: exported_data.csv")
            # write to a csv file
            csv_file = 'csv_data\{}'.format(csv_file_name)

            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(result)
            
    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection to the database closed successfully.")