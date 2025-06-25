def main():
    print("=== Number Cruncher ===")

    # 1. Ask for numbers (comma-separated)
    input_str = input("Enter numbers separated by commas (e.g. 10, 20, 30): ")

    # 2. Convert to list of floats
    try:
        numbers = [float(num.strip()) for num in input_str.split(",")]
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\n--- Results ---")
    print(f"Numbers: {numbers}")
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {round(sum(numbers) / len(numbers), 2)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")

    # 3. Show if each number is even/odd (only if integers)
    print("\nEven/Odd check (for whole numbers):")
    for num in numbers:
        if num.is_integer():
            if int(num) % 2 == 0:
                print(f"{int(num)} is Even")
            else:
                print(f"{int(num)} is Odd")
        else:
            print(f"{num} is not a whole number")

    print("\nDone!")

if __name__ == "__main__":
    main()
