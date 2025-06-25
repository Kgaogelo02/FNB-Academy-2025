def display_menu():
    print("\n=== Student Marks Viewer ===")
    print("1. View all students")
    print("2. View a student's marks by name")
    print("3. Show top scorer")
    print("4. Search for a mark in any student record")
    print("0. Exit")

def view_all_students(data):
    print("\n--- All Students ---")
    for student in data:
        name, marks = student
        print(f"{name}: {marks}")

def view_student_by_name(data):
    name = input("Enter student name: ").title()
    found = False
    for student in data:
        if student[0] == name:
            print(f"{name}'s marks: {student[1]}")
            found = True
            break
    if not found:
        print(f"No student named '{name}' found.")

def show_top_scorer(data):
    top_student = None
    top_total = -1
    for student in data:
        total = sum(student[1])
        if total > top_total:
            top_total = total
            top_student = student
    name, marks = top_student
    print(f"\nTop scorer is {name} with total marks: {top_total} ({marks})")

def search_mark(data):
    try:
        mark = int(input("Enter the mark to search for: "))
        found = False
        for name, marks in data:
            if mark in marks:
                print(f"{mark} found in {name}'s marks.")
                found = True
        if not found:
            print(f"No student has the mark {mark}.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    # Tuple of students, where each student is a tuple: (name, (math, science, english))
    students = (
        ("Kgaogelo", (85, 90, 88)),
        ("Mabutsi", (75, 80, 72)),
        ("Kgagara", (90, 92, 95)),
        ("Kay", (60, 70, 65)),
    )

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_students(students)
        elif choice == '2':
            view_student_by_name(students)
        elif choice == '3':
            show_top_scorer(students)
        elif choice == '4':
            search_mark(students)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
