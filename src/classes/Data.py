import mysql.connector
import os
from dotenv import load_dotenv

class Data:
    load_dotenv()
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

    @staticmethod
    def connect():
        """Establish a connection to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host=Data.MYSQL_HOST,
                database=Data.MYSQL_DATABASE,
                user=Data.MYSQL_USER,
                password=Data.MYSQL_PASSWORD
            )

            if connection.is_connected():
                return connection

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    @staticmethod
    def exec(sql):
        """Execute a raw SQL query and return the result."""
        connection = Data.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()
                return result
            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")
                return None
            finally:
                connection.close()
                print("MySQL connection is closed")
        else:
            return None

    @staticmethod
    def test():
        """Test the connection to the MySQL database."""
        connection = Data.connect()
        if connection:
            connection.close()
            print("MySQL connection was successful")

