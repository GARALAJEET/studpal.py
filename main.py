from auth_service import AuthService
from timetable import Timetable
from timetable_service import TimetableService
from  WalletService import WalletService 
from user import User
from expense import Expense

def main():
    auth_service = AuthService()
    wallet_service = WalletService()
    timetable_service = TimetableService()

    print("Welcome to StudPal!")
    print("1. Sign Up")
    print("2. Login")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email (optional): ")
        full_name = input("Enter full name (optional): ")
        user = User(username, password, email, full_name)
        auth_service.sign_up(user)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if auth_service.login(username, password):
            while True:
                print("\nMain Menu")
                print("1. Manage Timetable")
                print("2. Wallet & Expenses")
                print("3. Exit")
                option = input("Choose an option: ")

                if option == "1":
                    print("\nTimetable Management")
                    print("1. Add Entry")
                    print("2. view Time table")
                    print("3. Exit")
                    sub_option = input("Choose an option: ")
                    if sub_option == "1":
                        subject = input("Enter subject: ")
                        day_of_week = input("Enter day of the week: ")
                        location = input("Enter location: ")
                        description = input("Enter number of lectures: ")
                        timetable = Timetable(None, username, subject, day_of_week, location, description)
                        timetable_service.add_timetable_entry(timetable)
                    elif sub_option=="2":
                        timetable_service.viewTimeTable(username)
                    elif sub_option == "3":
                        break

                elif option == "2":
                    print("\nWallet & Expense Management")
                    print("1. Add Money to Wallet")
                    print("2. Add Expense")
                    print("3. View Expenses")
                    print("4. check Wallet Balance")
                    print("5. Exit")
                    wallet_option = input("Choose an option: ")

                    if wallet_option == "1":
                        amount = float(input("Enter amount to add: "))
                        wallet_service.add_money(username, amount)

                    elif wallet_option == "2":
                        amount = float(input("Enter expense amount: "))
                        category = input("Enter category (e.g., Food, Transport, Shopping): ")
                        description = input("Enter description: ")
                        wallet_service.add_expense(username, amount, category, description)

                    elif wallet_option == "3":
                        expenses = wallet_service.get_expenses(username)
                    elif wallet_option=="4":
                        wallet1=wallet_service.getBalance(username)
                    elif wallet_option == "5":
                        break

                elif option == "3":
                    break

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
