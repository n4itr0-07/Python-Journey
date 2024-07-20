
# Personal Finance Manager

Personal Finance Manager is a Python-based command-line application designed to help users track their income, expenses, and savings. It allows users to add transactions, view them, generate reports, and visualize spending habits.

## Features

1. **Add Income/Expense:**
   - Allows users to add a new transaction by specifying the date, type (Income/Expense), category, and amount.

2. **View Transactions:**
   - Displays all transactions stored in the database, ordered by date.

3. **Generate Reports:**
   - Summarizes the total income and expenses.

4. **Visualize Spending:**
   - Provides a bar chart visualization of expenses by category.

## Prerequisites

- Python 3.x
- MySQL server
- `mysql-connector-python` library
- `matplotlib` library

## Setup

1. **Install Python:**
   - Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Install MySQL:**
   - Download and install MySQL from the [official website](https://dev.mysql.com/downloads/).

3. **Install Required Python Libraries:**
   - Open a terminal and run the following commands:
     ```sh
     pip install mysql-connector-python
     pip install matplotlib
     ```

4. **Create MySQL Database and Table:**
   - Open MySQL Workbench or use the command line to run the following SQL commands:
     ```sql
     CREATE DATABASE finance_manager;
     USE finance_manager;
     CREATE TABLE transactions (
         id INT AUTO_INCREMENT PRIMARY KEY,
         date DATE,
         type ENUM('Income', 'Expense'),
         category VARCHAR(50),
         amount DECIMAL(10, 2)
     );
     ```

## Running the Application

1. **Clone the Repository:**
   - Clone this repository to your local machine or create a new directory and copy the `finance_manager.py` file into it.

2. **Configure Database Connection:**
   - Open the `finance_manager.py` file.
   - Replace `your_username` and `your_password` with your MySQL credentials in the following section:
     ```python
     conn = mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="finance_manager"
     )
     ```

3. **Run the Application:**
   - Open a terminal in the directory containing `finance_manager.py`.
   - Run the script by typing:
     ```sh
     python finance_manager.py
     ```

## Usage

Upon running the script, you will be presented with a menu:

```
****************************************
Personal Finance Manager
****************************************
1. Add Transaction
2. View Transactions
3. Generate Report
4. Visualize Spending
5. Exit
****************************************
Enter your choice:
```

### Options:

1. **Add Transaction:**
   - Prompts you to enter the date, type (Income/Expense), category, and amount for a new transaction.

2. **View Transactions:**
   - Displays all transactions stored in the database.

3. **Generate Report:**
   - Summarizes and displays the total income and expenses.

4. **Visualize Spending:**
   - Generates a bar chart visualization of expenses by category using `matplotlib`.

5. **Exit:**
   - Exits the application.

## Example Run

1. **Add an Income Transaction:**
   ```
   Enter your choice: 1
   Enter date (YYYY-MM-DD): 2024-07-20
   Enter type (Income/Expense): Income
   Enter category: Salary
   Enter amount: 5000
   Transaction added successfully.
   ```

2. **View Transactions:**
   ```
   Enter your choice: 2
   (1, '2024-07-20', 'Income', 'Salary', 5000.0)
   ```

3. **Add an Expense Transaction:**
   ```
   Enter your choice: 1
   Enter date (YYYY-MM-DD): 2024-07-21
   Enter type (Income/Expense): Expense
   Enter category: Groceries
   Enter amount: 200
   Transaction added successfully.
   ```

4. **View Transactions:**
   ```
   Enter your choice: 2
   (1, '2024-07-20', 'Income', 'Salary', 5000.0)
   (2, '2024-07-21', 'Expense', 'Groceries', 200.0)
   ```

5. **Generate Report:**
   ```
   Enter your choice: 3
   Income: 5000.0
   Expense: 200.0
   ```

6. **Visualize Spending:**
   ```
   Enter your choice: 4
   # A bar chart will be displayed showing the spending by category.
   ```

7. **Exit the Application:**
   ```
   Enter your choice: 5
   Exiting the program. Have a great day!
   ```



## Acknowledgements

- Thanks to the developers of [MySQL](https://www.mysql.com/) and [Python](https://www.python.org/) for providing the tools necessary to create this application.
- Special thanks to [matplotlib](https://matplotlib.org/) for the visualization library.
