import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


def create_connection():
    """Create a connection to the database."""
    db_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_DATABASE'),
    }

    connection = mysql.connector.connect(**db_config)
    return connection


def execute_query(connection, sql_query):
    """Execute a SQL query."""
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()


def close_connection(connection):
    """Close the database connection."""
    connection.close()
