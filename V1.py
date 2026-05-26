from datetime import datetime

def add_expense():

    date = datetime.now().strftime("%d-%m-%Y")

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    with open("expenses.txt", "a") as file:
        file.write(f"{date} | {category} | {amount}\n")
    
    print("Expense added successfully.\n")

def calculate_total():

    total = 0

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            amount = float(parts[2])
            total += amount

    return total

def view_expenses():

    with open("expenses.txt", "r") as file:

        content = file.read()

        print("\nSaved Expenses:\n")
        print(content)
    print(f"\nTotal Expenditure = {calculate_total()}\n")

while True:

    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()
    
    elif choice == 2:
        view_expenses()
    
    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.\n")
