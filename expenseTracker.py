import json
from datetime import datetime

# File to store expense data
EXPENSE_FILE = 'expenses.json'

# Load expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense(expenses):
    amount = float(input("Enter the amount: $"))
    category = input("Enter the category (e.g., Food, Transport): ")
    date_input = input("Enter the date (YYYY-MM-DD) or leave empty for today's date: ")

    if not date_input:
        date_input = datetime.today().strftime('%Y-%m-%d')
    
    expense = {
        'amount': amount,
        'category': category,
        'date': date_input
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("\nExpense added successfully!\n")

# View summary by category
def view_summary(expenses):
    category = input("Enter the category to view the total spending (e.g., Food): ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"\nTotal spending in category '{category}': ${total:.2f}\n")

# View total spending
def view_total_spending(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal overall spending: ${total:.2f}\n")

# View spending over time (daily, weekly, or monthly summaries)
def view_spending_over_time(expenses):
    print("\nChoose time summary:")
    print("1. Daily")
    print("2. Monthly")
    choice = input("Enter your choice (1 or 2): ")

    summary = {}
    if choice == '1':
        for exp in expenses:
            date = exp['date']
            summary[date] = summary.get(date, 0) + exp['amount']
        print("\nDaily Spending Summary:")
    elif choice == '2':
        for exp in expenses:
            month = exp['date'][:7]  # Extract YYYY-MM part for monthly summary
            summary[month] = summary.get(month, 0) + exp['amount']
        print("\nMonthly Spending Summary:")
    
    for period, total in summary.items():
        print(f"{period}: ${total:.2f}")
    print()

# Menu for the user to interact with
def expense_tracker():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View Summary by Category")
        print("3. View Total Spending")
        print("4. View Spending Over Time")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            view_total_spending(expenses)
        elif choice == '4':
            view_spending_over_time(expenses)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    expense_tracker()
