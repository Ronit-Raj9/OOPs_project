import mysql.connector
import csv
from mysql.connector import Error
import datetime

# Adds all entries present in csv_data/input_data.csv to the database
def add_to_db(csv_file_name):
    """
    Adds all entries present in the given CSV file to the database.
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

        formatted_date = datetime.date.today().strftime("%d-%m-%Y")

        if conn.is_connected():
            db = conn.get_server_info()
            print("Connected to database:", db)
            
            cursor = conn.cursor()

            print("Inserting CSV file to database...")

            csv_file = 'csv_data\{}'.format(csv_file_name)
            with open(csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)

                for row in csv_reader:
                    print(row)
                    row.append(formatted_date)
                    cursor.execute("""INSERT INTO `vehicle_details`
                                (SERIAL_NO, VEHICLE_NO, VEHICLE_TYPE, NAME, AGE, PHONE_NO, FINE, PREV_FINE, DATE)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)
                    conn.commit()


            # print the table
            cursor.execute("SELECT * FROM `vehicle_details`")
            result = cursor.fetchall()

            print("\nDatabase:")
            for row in result:
                print(row)
            print("")

    except Error as e:
        print("Error connnecting to the database")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nConnection to the database closed successfully.")