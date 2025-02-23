"""
A simple command line application to track personal finance
"""

import json

# Initial data structure to store income and expenses
financial_data = {
    "income": [],
    "expenses": []
}


def add_income(amount, description):
    """
    Add income to the financial data
    """
    financial_data["income"].append(
        {"amount": amount, "description": description})


def add_expense(amount, description):
    """
    Add expense to the financial data
    """
    financial_data["expenses"].append(
        {"amount": amount, "description": description})


def save_data(filename="financial_data.json"):
    """
    Save the financial data to a file
    """
    with open(filename, "w") as file:
        json.dump(financial_data, file)


def load_data(filename="financial_data.json"):
    """
    Load the financial data from a file
    """
    global financial_data
    try:
        with open(filename, "r") as file:
            financial_data = json.load(file)
    except FileNotFoundError:
        print("No existing file found. A new file will be created")


def show_menu():
    """
    Display the menu options
    """
    print("\n Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Save Data")
    print("4. load Data")
    print("5. View Financial Data")
    print("6. Exit")


def main():
    """
    Main entry point of the application
    """
    load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Entern income description: ")
            add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            add_expense(amount, description)
        elif choice == '3':
            save_data()
            print("Data saved successfully")
        elif choice == '4':
            load_data()
            print("Data loaded successfully")
        elif choice == '5':
            print(json.dumps(financial_data, indent=2))
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

