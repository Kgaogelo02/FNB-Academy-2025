def display_menu():
    print("\n=== Unique Hobby Collector ===")
    print("1. Enter hobbies for Person A")
    print("2. Enter hobbies for Person B")
    print("3. Show all unique hobbies (A ∪ B)")
    print("4. Show common hobbies (A ∩ B)")
    print("5. Show hobbies only in A (A - B)")
    print("6. Check if someone likes a hobby")
    print("0. Exit")

def input_hobbies(name):
    hobbies = input(f"Enter hobbies for {name} (comma separated): ")
    return set(h.strip().lower() for h in hobbies.split(","))

def main():
    hobbies_a = set()
    hobbies_b = set()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            hobbies_a = input_hobbies("Person A")
            print("Hobbies for A saved.")
        elif choice == '2':
            hobbies_b = input_hobbies("Person B")
            print("Hobbies for B saved.")
        elif choice == '3':
            print(f"All unique hobbies (A ∪ B): {hobbies_a.union(hobbies_b)}")
        elif choice == '4':
            print(f"Common hobbies (A ∩ B): {hobbies_a.intersection(hobbies_b)}")
        elif choice == '5':
            print(f"Hobbies only in A (A - B): {hobbies_a.difference(hobbies_b)}")
        elif choice == '6':
            hobby = input("Enter hobby to check: ").strip().lower()
            found = []
            if hobby in hobbies_a:
                found.append("A")
            if hobby in hobbies_b:
                found.append("B")
            if found:
                print(f"{hobby} is liked by: {', '.join(found)}")
            else:
                print(f"No one likes '{hobby}'.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
