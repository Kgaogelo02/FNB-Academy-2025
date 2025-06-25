def display_menu():
    print("\n=== Student Gradebook ===")
    print("1. Add a student and grade")
    print("2. Update a student's grade")
    print("3. Delete a student")
    print("4. View all students and grades")
    print("5. View a specific student's grade")
    print("6. View class average")
    print("0. Exit")

def show_all(gradebook):
    if not gradebook:
        print("Gradebook is empty.")
    else:
        print("\n--- All Students ---")
        for name, grade in gradebook.items():
            print(f"{name}: {grade}")

def main():
    gradebook = {}

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ").title()
            if name in gradebook:
                print("Student already exists.")
            else:
                try:
                    grade = float(input(f"Enter grade for {name}: "))
                    gradebook[name] = grade
                    print(f"{name} added with grade {grade}.")
                except ValueError:
                    print("Invalid grade.")

        elif choice == '2':
            name = input("Enter student name to update: ").title()
            if name in gradebook:
                try:
                    new_grade = float(input("Enter new grade: "))
                    gradebook[name] = new_grade
                    print(f"{name}'s grade updated to {new_grade}.")
                except ValueError:
                    print("Invalid grade.")
            else:
                print(f"{name} not found.")

        elif choice == '3':
            name = input("Enter student name to delete: ").title()
            if name in gradebook:
                del gradebook[name]
                print(f"{name} removed.")
            else:
                print(f"{name} not found.")

        elif choice == '4':
            show_all(gradebook)

        elif choice == '5':
            name = input("Enter student name: ").title()
            grade = gradebook.get(name)
            if grade is not None:
                print(f"{name}'s grade: {grade}")
            else:
                print(f"{name} not found.")

        elif choice == '6':
            if gradebook:
                avg = sum(gradebook.values()) / len(gradebook)
                print(f"Class average: {round(avg, 2)}")
            else:
                print("No grades available to calculate average.")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
