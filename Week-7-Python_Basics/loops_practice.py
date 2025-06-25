def display_menu():
    print("\n=== Loops Practice Station ===")
    print("1. Count from 1 to N using a for loop")
    print("2. Sum numbers until user enters 0 (while loop)")
    print("3. Reverse a word using a loop")
    print("4. Print even numbers between 1 and N")
    print("5. Simple star pattern")
    print("0. Exit")

def count_up():
    n = int(input("Enter a number N: "))
    print("Counting from 1 to", n)
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def sum_until_zero():
    total = 0
    while True:
        num = float(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    print(f"Total sum: {total}")

def reverse_word():
    word = input("Enter a word: ")
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word  # building in reverse
    print(f"Reversed word: {reversed_word}")

def even_numbers():
    n = int(input("Print even numbers up to N: "))
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue
        print(i, end=" ")
    print()

def star_pattern():
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print("*" * i)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            count_up()
        elif choice == '2':
            sum_until_zero()
        elif choice == '3':
            reverse_word()
        elif choice == '4':
            even_numbers()
        elif choice == '5':
            star_pattern()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
