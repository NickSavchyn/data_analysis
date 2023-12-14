import os

import mysql.connector

# db connection
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


with open('sql_script,sql.sql', 'r') as file:
    sql_query = file.read()

try:
    # sql query
    cursor.execute(sql_query)

    result = cursor.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:

    cursor.close()
    connection.close()
