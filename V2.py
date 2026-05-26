from datetime import datetime

budgets = {}

def set_budget():
    category = input("Enter category: ").title()
    limit = float(input("Enter budget limit: "))
    budgets[category] = limit

    print(f"\nBudget set for {category}: {limit}\n")

def add_expense():

    date = datetime.now().strftime("%d-%m-%Y")

    category = input("Enter category: ").title()
    amount = float(input("Enter amount: "))
    reason = input("Enter Reason: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date} | {category} | {amount} | {reason}\n")
    
    print("Expense added successfully.\n")

def calculate_total():

    total = 0

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            amount = float(parts[2])
            total += amount

    return total

def category_total():
    totals = {}

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")

            category = parts[1]
            amount = float(parts[2])

            if category in totals:
                totals[category] += amount
            
            else:
                totals[category] = amount
    
    print("\nCategory wise Totals:\n")

    for category,total in totals.items():
        print(f"{category} = {total}")

def view_expenses():

    with open("expenses.txt", "r") as file:

        print("\nSaved Expenses:\n")
        print("-" * 70)

        for line in file:
            parts = line.strip().split(" | ")
            print(f"Date: {parts[0]}")
            print(f"Category: {parts[1]}")
            print(f"Amount: {parts[2]}")
            print(f"Reason: {parts[3]}")
            print("-" * 70)

def search_reason():
    search = input("Enter reason to search: ").title()

    found = False
    
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            reason = parts[3].title()

            if search == reason:
                print("-" * 70)
                print(f"Date: {parts[0]}")
                print(f"Category: {parts[1]}")
                print(f"Amount: {parts[2]}")
                print(f"Reason: {parts[3]}")

                found = True
            
    if not found:
        print("\nNo matching expenses found.\n")

def search_category():
    search = input("Enter category to search: ").title()

    found = False
    
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            category = parts[1].title()

            if search == category:
                print("-" * 70)
                print(f"Date: {parts[0]}")
                print(f"Category: {parts[1]}")
                print(f"Amount: {parts[2]}")
                print(f"Reason: {parts[3]}")

                found = True
            
    if not found:
        print("\nNo matching expenses found.\n")

def check_budget_limits():
    totals = {}

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")

            category = parts[1]
            amount = float(parts[2])

            if category in totals:
                totals[category] += amount
            
            else:
                totals[category] = amount
    
    print("\nBudget Warnings:\n")
    for category, total in totals.items():
        if category in budgets:
            if total > budgets[category]:
                print(f"Warning: {category} budget exceeded!")
                print(f"spent: {total}")
                print(f"budget: {budgets[category]}")
                print("-" * 70)


while True:

    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Total Expenditure")
    print("4. Category Wise Totals")
    print("5. Set Budget")
    print("6. Budget Warnings")
    print("7. Search by Reason")
    print("8. Search by Category")
    print("9. Exit")

    choice = input("Enter your choice: ").title()

    if choice == "1":
        add_expense()
    
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        print(f"\nTotal Expenditure = {calculate_total()}\n")
    
    elif choice == "4":
        category_total()
    
    elif choice == "5":
        set_budget()
    
    elif choice == "6":
        check_budget_limits()

    elif choice == "7":
        search_reason()
    
    elif choice == "8":
        search_category()

    elif choice == "9":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.\n")
