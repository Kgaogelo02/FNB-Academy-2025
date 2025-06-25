def display_menu():
    print("\n=== Grocery List Manager ===")
    print("1. Show grocery list")
    print("2. Add item")
    print("3. Insert item at position")
    print("4. Remove item by name")
    print("5. Pop last item")
    print("6. Sort items (A-Z)")
    print("7. Reverse list")
    print("8. Check if item exists")
    print("0. Exit")

def show_list(grocery_list):
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Grocery List:")
        for i, item in enumerate(grocery_list):
            print(f"{i + 1}. {item}")

def main():
    grocery_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            show_list(grocery_list)

        elif choice == '2':
            item = input("Enter item to add: ")
            grocery_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == '3':
            item = input("Enter item to insert: ")
            pos = int(input("Enter position (starting at 1): "))
            if 1 <= pos <= len(grocery_list) + 1:
                grocery_list.insert(pos - 1, item)
                print(f"'{item}' inserted at position {pos}.")
            else:
                print("Invalid position.")

        elif choice == '4':
            item = input("Enter item to remove: ")
            if item in grocery_list:
                grocery_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found.")

        elif choice == '5':
            if grocery_list:
                removed = grocery_list.pop()
                print(f"Removed last item: {removed}")
            else:
                print("List is empty.")

        elif choice == '6':
            grocery_list.sort()
            print("List sorted A-Z.")

        elif choice == '7':
            grocery_list.reverse()
            print("List order reversed.")

        elif choice == '8':
            item = input("Enter item to check: ")
            print(f"'{item}' is in the list? {'Yes' if item in grocery_list else 'No'}")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
