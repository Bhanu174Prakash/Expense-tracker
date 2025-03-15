import csv
import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Function to initialize CSV file
def initialize_file():
    try:
        with open(EXPENSE_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass  # File already exists, no need to create it

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ") or datetime.date.today().strftime('%Y-%m-%d')
    amount = input("Enter amount spent: ")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    description = input("Enter description: ")

    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return

        print("\nAll Expenses:")
        for expense in expenses:
            print(f"Date: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}, Description: {expense[3]}")
        print("\n")

    except FileNotFoundError:
        print("No expenses found. Start adding expenses first.\n")

# Function to show category-wise expense summary
def category_summary():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return
        
        summary = {}
        for expense in expenses:
            category = expense[2]
            amount = float(expense[1])
            summary[category] = summary.get(category, 0) + amount
        
        print("\nCategory-wise Expense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
        print("\n")

    except FileNotFoundError:
        print("No expenses found.\n")

# Function to show monthly expense summary
def monthly_summary():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return

        summary = {}
        for expense in expenses:
            month = expense[0][:7]  # Extract YYYY-MM from date
            amount = float(expense[1])
            summary[month] = summary.get(month, 0) + amount
        
        print("\nMonthly Expense Summary:")
        for month, total in summary.items():
            print(f"{month}: ${total:.2f}")
        print("\n")

    except FileNotFoundError:
        print("No expenses found.\n")

# Main menu loop
def main():
    initialize_file()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye! Happy Budgeting!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Expense Tracker
if __name__ == "__main__":
    main()
