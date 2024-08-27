import mysql.connector
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MySQL connection details from environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
