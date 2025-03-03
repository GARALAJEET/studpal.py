from database_connection import DatabaseConnection
from user import User

class AuthService:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()

    def sign_up(self, user):
        if not self.connection:
            print("Failed to connect to the database.")
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = %s", (user.username,))
            if cursor.fetchone():
                print("Username already exists.")
                return False

            cursor.execute("INSERT INTO Users (username, password, email, fullName) VALUES (%s, %s, %s, %s)",
                           (user.username, user.password, user.email, user.full_name))
            self.connection.commit()
            print("User signed up successfully.")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def login(self, username, password):
        if not self.connection:
            print("Failed to connect to the database.")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
            if cursor.fetchone():
                print("Login successful!")
                return True
            else:
                print("Invalid username or password.")
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
