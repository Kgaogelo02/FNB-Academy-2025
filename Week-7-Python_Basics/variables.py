def main():
    print("=== Personal Budget Calculator ===")

    # 1. Declare variables
    monthly_income = float(input("Enter your monthly income (R): "))
    rent = float(input("Enter your rent amount (R): "))
    groceries = float(input("Enter your groceries budget (R): "))
    transport = float(input("Enter your transport cost (R): "))

    # 2. Calculate total expenses and savings
    total_expenses = rent + groceries + transport
    savings = monthly_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Income: R{monthly_income}")
    print(f"Rent: R{rent}")
    print(f"Groceries: R{groceries}")
    print(f"Transport: R{transport}")
    print(f"Total Expenses: R{total_expenses}")
    print(f"Estimated Savings: R{round(savings, 2)}")

    # 3. Update a variable
    print("\nOops! You forgot your WiFi bill.")
    wifi = float(input("Enter WiFi cost (R): "))
    total_expenses += wifi
    savings = monthly_income - total_expenses

    print("\n--- Updated Budget ---")
    print(f"New Total Expenses: R{total_expenses}")
    print(f"New Estimated Savings: R{round(savings, 2)}")

    # 4. Swap example (just for learning)
    print("\n--- Bonus: Swapping Variables....")
    a = 5
    b = 10
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After Swap: a = {a}, b = {b}")

    print("\nDone!")

if __name__ == "__main__":
    main()
