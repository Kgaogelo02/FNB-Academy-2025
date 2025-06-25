def main():
    print("=== Numeric Operators Practice ===")

    # 1. Input numbers
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))

    # 2. Arithmetic Operators
    print("\n--- Arithmetic Operators ---")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b if b != 0 else 'Undefined (division by zero)'}")
    print(f"a % b = {a % b if b != 0 else 'Undefined (mod by zero)'}")
    print(f"a // b = {a // b if b != 0 else 'Undefined (floor division by zero)'}")
    print(f"a ** b = {a ** b}")

    # 3. Comparison Operators
    print("\n--- Comparison Operators ---")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a >= b: {a >= b}")
    print(f"a <= b: {a <= b}")

    # 4. Assignment Operators
    print("\n--- Assignment Operators Demo ---")
    x = a
    print(f"x = {x}")
    x += b
    print(f"x += b -> {x}")
    x -= b
    print(f"x -= b -> {x}")
    x *= b
    print(f"x *= b -> {x}")
    if b != 0:
        x /= b
        print(f"x /= b -> {x}")
    else:
        print("x /= b -> Skipped (division by zero)")

    # 5. Logical Operators
    print("\n--- Logical Operators ---")
    print(f"(a > 0) and (b > 0): {(a > 0) and (b > 0)}")
    print(f"(a > 0) or (b > 0): {(a > 0) or (b > 0)}")
    print(f"not (a > 0): {not (a > 0)}")

    print("\nDone!")

if __name__ == "__main__":
    main()
