from database_connection import DatabaseConnection
from expense import Expense
import mysql.connector
from datetime import datetime

class WalletService:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()
    def getBalance(self,username):
            cursor = self.connection.cursor()
            cursor.execute("SELECT wallet_balance FROM Users WHERE username = %s", (username,))
            result = cursor.fetchone()
            print(f"Balance : ₹{result}")

    def add_money(self, username, amount):
        """Adds money to the user's wallet."""
        if amount <= 0:
            print("Amount must be positive.")
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Users SET wallet_balance = wallet_balance + %s WHERE username = %s", (amount, username))
            self.connection.commit()
            print(f"Added ₹{amount} to {username}'s wallet.")
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def add_expense(self, username, amount, category, description):
        """Adds a daily expense for the user and updates the wallet balance."""
        if amount <= 0:
            print("Expense amount must be positive.")
            return False

        try:
            # Check if user has enough balance
            cursor = self.connection.cursor()
            cursor.execute("SELECT wallet_balance FROM Users WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result and result[0] >= amount:
                # Insert expense record
                cursor.execute("INSERT INTO Expenses (username, amount, category, date, description) VALUES (%s, %s, %s, %s, %s)",
                               (username, amount, category, datetime.now().date(), description))
                
                # Deduct amount from wallet
                cursor.execute("UPDATE Users SET wallet_balance = wallet_balance - %s WHERE username = %s", (amount, username))

                self.connection.commit()
                print(f"Expense of ₹{amount} added under '{category}' for {username}.")
                return True
            else:
                print("Insufficient balance!")
                return False

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def get_expenses(self, username):
        """Fetches all expenses of a user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, amount, category, date, description FROM Expenses WHERE username = %s", (username,))
            expenses = cursor.fetchall()
            if not expenses:
                print("No expenses found.")
                # return []

            expanse_list=f"expanse_List.txt"
            with open(expanse_list,"w")as expanse_File:
                expanse_File.write("  Expenses List  \n")
                expanse_File.write("---------------------------------\n")
                # expanse_File.write(f"expenses: {expenses[0]}\n")
                for expense in expenses:
                    expanse_File.write(f"Amount: {expense[1]}  Category:{expense[4]}  Date:{expense[3]}   Description: {expense[4]}\n")
                expanse_File.write("---------------------------------\n")
                print("📄statement Printed")

            # return [Expense(username, row[1], row[2], row[3], row[4], expense_id=row[0]) for row in expenses]


        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []