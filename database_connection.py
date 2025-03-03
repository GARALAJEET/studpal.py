import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

class DatabaseConnection:
    def __init__(self):
        self.host = "localhost"
        self.database = "studpal"
        self.user = "root"
        self.password = "rio2603"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
