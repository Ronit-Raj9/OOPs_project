import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host = "0.tcp.in.ngrok.io",
        port = 14155,
        user = "root",
        passwd = "",
        database = "oops_db"
    )

    if conn.is_connected():
        db = conn.get_server_info()
        print("Connected to MySQL Server: ", db)
        cursor = conn.cursor()

        cursor.execute("select * from `vehicle_details`")
        result = cursor.fetchall()

        for row in result:
            print(row)
            # print(row[1])
            
except Error as e:
    print("Error connecting to database.")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection to the database closed successfully.")

