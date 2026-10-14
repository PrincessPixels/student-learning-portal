"""
Student Learning Portal
PROG211 - Object-Oriented Programming 1

A beginner-friendly console program that stores sample student records
in a list. It uses fictional data only and does not request sensitive
personal information.
"""

class Student:
    """Represent one student and their learning information."""

    total_students = 0  # Class attribute shared by all Student objects

    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.progress = "Not started"
        Student.total_students += 1

    def update_progress(self, new_progress):
        """Instance method: update this student's learning progress."""
        allowed_progress = ["Not started", "In progress", "Completed"]
        if new_progress not in allowed_progress:
            return False
        self.progress = new_progress
        return True

    def display_info(self):
        """Instance method: return this student's details."""
        return (
            f"ID: {self.student_id} | Name: {self.name} | "
            f"Course: {self.course} | Progress: {self.progress}"
        )

    @classmethod
    def create_demo_student(cls, student_id, name, course):
        """Class method: create a Student object using the class."""
        return cls(student_id, name, course)


class LearningPortal:
    """Manage student objects in one list."""

    def __init__(self):
        self.students = []  # The one required data structure: a list

    def add_student(self, student):
        """Add a student unless the ID is already in use."""
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("A student with that ID already exists.")
                return False
        self.students.append(student)
        print("Student added successfully.")
        return True

    def display_students(self):
        """Display all students stored in the list."""
        if not self.students:
            print("No student records have been added yet.")
            return
        print("\n--- Student Records ---")
        for student in self.students:
            print(student.display_info())

    def find_student(self, student_id):
        """Find and return a student by ID, or None if not found."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    portal = LearningPortal()

    # Sample records use fictional names and non-sensitive information.
    demo_student = Student.create_demo_student(
        "ST001", "Aminata Kamara", "Introduction to Python"
    )
    portal.add_student(demo_student)

    second_student = Student("ST002", "Joseph Conteh", "Database Basics")
    portal.add_student(second_student)

    print("\nWelcome to the Student Learning Portal")
    print("1. Add student")
    print("2. View all students")
    print("3. Update student progress")
    print("4. Exit")

    while True:
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            course = input("Enter course name: ").strip()

            if not student_id or not name or not course:
                print("All fields are required.")
                continue

            student = Student(student_id, name, course)
            portal.add_student(student)

        elif choice == "2":
            portal.display_students()
            print(f"Total Student objects created: {Student.total_students}")

        elif choice == "3":
            student_id = input("Enter student ID: ").strip()
            student = portal.find_student(student_id)

            if student is None:
                print("Student ID not found.")
                continue

            print("Progress options: Not started, In progress, Completed")
            new_progress = input("Enter new progress exactly as shown: ").strip()
            if student.update_progress(new_progress):
                print("Progress updated successfully.")
            else:
                print("Invalid progress option. No changes were made.")

        elif choice == "4":
            print("Thank you for using the Student Learning Portal.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
