# Student Performance Analyzer

students = []  # list of dictionaries


# Function to add a student
def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))
    attendance = int(input("Enter attendance percentage: "))

    student = {
        "name": name,
        "marks": marks,
        "attendance": attendance
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to display all students
def display_students():
    if not students:
        print("No student records available.\n")
        return

    print("\nStudent Records:")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}, Attendance: {s['attendance']}%")
    print()


# Function to calculate statistics
def calculate_statistics():
    if not students:
        print("No data to analyze.\n")
        return

    marks_list = [s["marks"] for s in students]

    avg = sum(marks_list) / len(marks_list)
    maximum = max(marks_list)
    minimum = min(marks_list)

    print(f"\nClass Average Marks: {avg:.2f}")
    print(f"Highest Marks: {maximum}")
    print(f"Lowest Marks: {minimum}\n")


# Function to rank students (using sorting)
def rank_students():
    if not students:
        print("No data to rank.\n")
        return

    ranked = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("\nStudent Rankings:")
    rank = 1
    for s in ranked:
        print(f"Rank {rank}: {s['name']} - {s['marks']} marks")
        rank += 1
    print()


# Function to search student by name
def search_student():
    if not students:
        print("No student records available.\n")
        return

    key = input("Enter student name to search: ").lower()

    for s in students:
        if s["name"].lower() == key:
            print(f"\nFound Student:")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Attendance: {s['attendance']}%\n")
            return

    print("Student not found.\n")


# Menu-driven program
def main():
    while True:
        print("==== Student Performance Analyzer ====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Statistics")
        print("4. Rank Students")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_statistics()
        elif choice == "4":
            rank_students()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
