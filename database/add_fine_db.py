import mysql.connector
import csv
from mysql.connector import Error

def add_fine(id, fine_amt):
    """
    Adds fine to the specified ID.
    Prints appropriate message if the ID is not found.
    Parameters: ID(int), fine_amt(int)
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

            fine_id = id
            new_fine = fine_amt

            select_query = "SELECT * FROM vehicle_details WHERE SERIAL_NO = {}".format(fine_id)
            cursor.execute(select_query)
            row = cursor.fetchone()

            if row:
                print("Row found.")
                print(row)

                fine = row[6]
                old_fine = row[7]
                total_old_fine = fine + old_fine

                print("Adding fine...")
                fine_query = '''
                UPDATE vehicle_details
                SET FINE={}, PREV_FINE={}
                WHERE SERIAL_NO={};
                '''.format(new_fine, total_old_fine, fine_id)

                cursor.execute(fine_query)
                conn.commit()
            
            else:
                print("Row with ID", fine_id, "not found.")

    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nConnection to the database closed successfully.")
            
# driver code - example
print("Adding fine of Rs. 10 to ID: 1009\n")
add_fine(1009, 10)