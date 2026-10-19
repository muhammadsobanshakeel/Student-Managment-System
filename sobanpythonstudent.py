
class Student:
    def __init__(self, name, roll_no, marks, total_marks=100):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.total_marks = total_marks

    def percentage(self):
        return (self.marks / self.total_marks) * 100

    def display(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}/{self.total_marks}")
        print(f"Percentage: {self.percentage():.2f}%")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        roll_no = input("Enter roll number: ").strip()

        if not roll_no:
            print("Roll number cannot be empty!")
            return

        if any(s.roll_no == roll_no for s in self.students):
            print("This roll number already exists!")
            return

        try:
            total = float(input("Enter total marks: "))
            marks = float(input("Enter obtained marks: "))

            if total <= 0 or marks < 0 or marks > total:
                print("Invalid marks!")
                return

        except ValueError:
            print("Please enter valid numbers!")
            return

        student = Student(name, roll_no, marks, total)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        roll_no = input("Enter roll number to search: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student not found!")

    def delete_student(self):
        roll_no = input("Enter roll number to delete: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

    def menu(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Please select 1-5.")


app = StudentManagementSystem()
app.menu()
