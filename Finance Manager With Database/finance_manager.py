import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # replace with your MySQL username
    password="Salik@123",  # replace with your MySQL password
    database="finance_manager"
)
c = conn.cursor()

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    type_ = input("Enter type (Income/Expense): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    c.execute("INSERT INTO transactions (date, type, category, amount) VALUES (%s, %s, %s, %s)", 
              (date, type_, category, amount))
    conn.commit()
    print("Transaction added successfully.")

def print_separator():
    print("\n" + "*" * 40 + "\n")

def view_transactions():
    c.execute("SELECT * FROM transactions ORDER BY date")
    rows = c.fetchall()
    for row in rows:
        print(row)

def generate_report():
    c.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
    rows = c.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]}")

def visualize_spending():
    c.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
    rows = c.fetchall()
    categories = [row[0] for row in rows]
    amounts = [row[1] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Amount Spent')
    plt.title('Spending by Category')
    plt.show()

def main():
    while True:
        print("Personal Finance Manager")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Visualize Spending")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_transaction()
        elif choice == 2:
            view_transactions()
        elif choice == 3:
            generate_report()
        elif choice == 4:
            visualize_spending()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
