# StudPal - A Student Productivity and Expense Management Application

## Overview
StudPal is a console-based application designed to help students manage their daily schedules and financial expenses effectively. It integrates a timetable management system, user authentication, a wallet feature, and expense tracking, all powered by a MySQL database.

## Features
### 1. User Authentication
- Users can **sign up** with a username, password, email, and full name.
- Users can **log in** with their credentials.
- Authentication is managed via the `AuthService` class.

### 2. Timetable Management
- Users can **add timetable entries** including subjects, lecture timings, and locations.
- Users can **view their timetable**.
- Managed through `TimetableService` and `TimetableDAO`.

### 3. Wallet & Expense Management
- Users can **add money** to their wallet.
- Users can **add expenses** and categorize them (e.g., Food, Transport, Shopping).
- Users can **view their expenses and check their wallet balance**.
- Managed via `WalletService` and `Expense` classes.

## Project Structure
```
StudPal/
│── auth_service.py        # Handles user authentication (sign-up & login)
│── database_connection.py # Manages MySQL database connection
│── expense.py             # Defines the Expense class
│── main.py                # Entry point of the application
│── my_array_list.py       # Custom implementation of an array list
│── timetable.py           # Defines the Timetable class
│── timetable_dao.py       # Database operations for the timetable
│── timetable_service.py   # Business logic for managing timetables
│── user.py                # Defines the User class
│── WalletService.py       # Handles wallet transactions and expenses
```

## Setup and Installation
### Prerequisites
- Python 3.x
- MySQL Server
- Required Python modules: `mysql-connector-python`

### Database Setup
1. Create a MySQL database named `studpal`.
2. Create the necessary tables:
```sql
CREATE TABLE Users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    fullName VARCHAR(100),
    wallet_balance DECIMAL(10,2) DEFAULT 0
);

CREATE TABLE Expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    amount DECIMAL(10,2),
    category VARCHAR(50),
    date DATE,
    description TEXT,
    FOREIGN KEY (username) REFERENCES Users(username)
);

CREATE TABLE college_timetable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    day VARCHAR(20),
    time VARCHAR(20),
    subject VARCHAR(100),
    number_of_lectures INT,
    FOREIGN KEY (username) REFERENCES Users(username)
);
```

### Running the Application
1. Clone the repository or download the source code.
2. Install required dependencies:
   ```bash
   pip install mysql-connector-python
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Run the program and follow the on-screen prompts to **sign up or log in**.
- After logging in, navigate through the **Timetable Management** and **Wallet & Expenses** options.
- Use **Timetable Management** to schedule lectures.
- Use **Wallet & Expenses** to track and manage your expenses.

## Future Enhancements
- Implement a **graphical user interface (GUI)**.
- Add **budget tracking and analytics**.
- Introduce **notification and reminder features**.

## Author
Developed by Rio as part of the StudPal project.



