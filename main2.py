import datetime
import json

# File to store expenses
EXPENSES_FILE = "expenses.json"

# Load expenses from file
try:
    with open(EXPENSES_FILE, "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    expenses = []


def save_expenses():
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(date, amount, category, description):
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    })
    save_expenses()
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    for expense in expenses:
        print(
            f"Date: {expense['date']}, Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    print()


def filter_expenses(category=None, start_date=None, end_date=None):
    filtered = expenses
    if category:
        filtered = [e for e in filtered if e["category"] == category]
    if start_date and end_date:
        filtered = [e for e in filtered if start_date <= datetime.datetime.strptime(e["date"], "%Y-%m-%d") <= end_date]

    if not filtered:
        print("No matching expenses found.\n")
    else:
        for expense in filtered:
            print(
                f"Date: {expense['date']}, Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    print()


def summarize_expenses():
    category_totals = {}
    total_expense = 0

    for expense in expenses:
        total_expense += expense["amount"]
        if expense["category"] in category_totals:
            category_totals[expense["category"]] += expense["amount"]
        else:
            category_totals[expense["category"]] = expense["amount"]

    print("Expense Summary:")
    for category, total in category_totals.items():
        print(f"{category}: ${total}")
    print(f"Total Expenses: ${total_expense}\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Summarize Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Enter category to filter (leave blank for all): ") or None
            start_date_str = input("Enter start date (YYYY-MM-DD) or leave blank: ")
            end_date_str = input("Enter end date (YYYY-MM-DD) or leave blank: ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d") if start_date_str else None
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else None
            filter_expenses(category, start_date, end_date)
        elif choice == "4":
            summarize_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
