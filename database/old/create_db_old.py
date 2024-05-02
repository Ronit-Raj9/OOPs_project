import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "oops_db"
    )

    if conn.is_connected():
        db = conn.get_server_info()
        print("Connected to database:", db)
        
        cursor = conn.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS vehicle_details(
        SERIAL_NO INT PRIMARY KEY,
        VEHICLE_NO VARCHAR(20),
        VEHICLE_TYPE VARCHAR(20),
        NAME VARCHAR(30),
        AGE INT(5),
        PHONE_NO INT(12),
        FINE INT(10),
        PREV_FINE INT(10)
        DATE VARCHAR(50)
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()

        print("\nTable:")
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