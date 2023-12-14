import numpy as np
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get database configuration from environment variables
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}



def retrieve_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql_query = "SELECT numeric_column FROM your_table_name"
    cursor.execute(sql_query)

    data = cursor.fetchall()
    connection.close()

    return data


def analyze_data(data):

    numeric_data = np.array(data)


    mean_value = np.mean(numeric_data)
    median_value = np.median(numeric_data)
    std_deviation = np.std(numeric_data)


    print("Numeric Data:", numeric_data)
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Standard Deviation:", std_deviation)


if __name__ == "__main__":

    data_from_db = retrieve_data()

    analyze_data(data_from_db)
