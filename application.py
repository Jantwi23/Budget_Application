from utility import create_login, login
from data_storage import data, save_data

def add_expense():
    """Add an expense to the tracker."""
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    data["expenses"].append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")
    save_data(data)

def delete_expense():
    """Delete an expense."""
    date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    initial_length = len(data["expenses"])
    data["expenses"] = [expense for expense in data["expenses"] if expense["date"] != date]
    print("Expense deleted successfully." if len(data["expenses"]) < initial_length else "No expense found.")
    save_data(data)

def view_expenses():
    """View all expenses."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        for expense in data["expenses"]:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")

def set_budget():
    """Set a budget for a category."""
    category = input("Enter category: ")
    limit = float(input("Enter budget limit: "))
    data["budgets"][category] = {"limit": limit, "spent": 0}
    print(f"Budget set for {category}: ${limit}")
    save_data(data)

def update_budget():
    """Update the budget for a category."""
    category = input("Enter category to update: ")
    if category in data["budgets"]:
        limit = float(input("Enter new budget limit: "))
        data["budgets"][category]["limit"] = limit
        print(f"Budget for {category} updated to ${limit}")
    else:
        print("Category not found.")
    save_data(data)

def view_budgets():
    """View all budgets."""
    if not data["budgets"]:
        print("No budgets set yet.")
    else:
        for category, details in data["budgets"].items():
            print(f"Category: {category}, Limit: ${details['limit']}, Spent: ${details['spent']}")

def generate_summary_report():
    """Generate a summary report of expenses."""
    summary = {}
    for expense in data["expenses"]:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    for category, total in summary.items():
        print(f"Category: {category}, Total Spent: ${total}")

def generate_monthly_report():
    """Generate a monthly spending report."""
    month = input("Enter the month (YYYY-MM): ")
    monthly_expenses = [expense for expense in data["expenses"] if expense["date"].startswith(month)]
    if not monthly_expenses:
        print("No expenses found for this month.")
    else:
        for expense in monthly_expenses:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")

def check_budget_alerts():
    """Check budget alerts for overspending."""
    for expense in data["expenses"]:
        category = expense["category"]
        if category in data["budgets"]:
            data["budgets"][category]["spent"] += expense["amount"]
            if data["budgets"][category]["spent"] >= data["budgets"][category]["limit"]:
                print(f"ALERT: Spending in {category} has exceeded the limit!")
    save_data(data)

def export_expenses():
    """Export expenses to a TXT file."""
    with open("expenses.txt", "w") as file:
        for expense in data["expenses"]:
            file.write(f"Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}\n")
    print("Expenses exported to expenses.txt")

def main_menu():
    """Main menu for the Smart Budget Tracker."""
    while True:
        print("\n--- Smart Budget Tracker ---")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View All Expenses")
        print("4. Set Budget for Category")
        print("5. Update Budget for Category")
        print("6. Generate Expense Summary Report")
        print("7. Generate Monthly Spending Report")
        print("8. Check Budget Alerts")
        print("9. View All Budgets")
        print("10. Export Expenses to TXT file")
        print("11. Logout")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            delete_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            update_budget()
        elif choice == "6":
            generate_summary_report()
        elif choice == "7":
            generate_monthly_report()
        elif choice == "8":
            check_budget_alerts()
        elif choice == "9":
            view_budgets()
        elif choice == "10":
            export_expenses()
        elif choice == "11":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def start_program():
    """Handle login, account creation, and main program flow."""
    while True:
        print("\n--- Welcome to Smart Budget Tracker ---")
        print("1. Create Login")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_login()
        elif choice == "2":
            if login():
                main_menu()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start_program()
