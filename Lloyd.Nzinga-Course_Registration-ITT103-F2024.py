students = {}  # {student_id: {"name": name, "courses": {course_id: balance}}}
courses = {}   # {course_id: {"name": name, "fee": fee}}

# OOP principles
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id  # Unique identifier for each course
        self.name = name            # Name of the course
        self.fee = fee              # Cost of the course
        self.students = []          # List of enrolled students

    def add_student(self, student):
        self.students.append(student)  # Add a student to the course
        return True


class Student:
    def __init__(self, student_id, name, email, courses=None, balance=0):
        self.student_id = student_id  # Unique identifier for each student
        self.name = name              # Student's name
        self.email = email            # Contact email
        self.courses = courses if courses else []  # List of enrolled courses
        self.balance = balance        # Current balance


class RegistrationSystem:
    def __init__(self):
        self.courses = []    # List of available courses
        self.students = {}   # Dictionary of registered students

    def add_course(self):
        course_id = input("Enter Course ID: ")
        if any(course.course_id == course_id for course in self.courses):
            print(f"Error: Course ID {course_id} already exists.")
            return
        name = input("Enter Course Name: ")
        fee = float(input("Enter Course Fee: "))
        course = Course(course_id, name, fee)
        self.courses.append(course)
        print(f"Course '{name}' added successfully.")

    def register_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Error: Student ID already exists.")
            return
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        student = Student(student_id, name, email)
        self.students[student_id] = student
        print(f"Student '{name}' successfully registered.")

    def show_registered_students(self):
        print("Registered Students:")
        for student_id, student in self.students.items():
            print(f"{student_id} - {student.name} (Email: {student.email})")

    def enroll_in_course(self):
        student_id = input("Enter Student ID: ")
        student = self.students.get(student_id)
        if not student:
            print("Error: Student not found.")
            return
        course_id = input("Enter Course ID: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Error: Course not found.")
            return
        course.add_student(student)
        student.courses.append(course)
        student.balance += course.fee
        print(f"Student '{student.name}' enrolled in '{course.name}' balance: '{student.balance}'.")

    def calculate_payment(self):
        student_id = input("Enter Student ID: ")
        student = self.students.get(student_id)
        if not student:
            print("Error: Student not found.")
            return
        print(f"Outstanding Balance: {student.balance}")
        payment = float(input("Enter Payment Amount: "))
        if payment < 0.4 * student.balance:
            print("Error: Payment must be at least 40% of the outstanding balance.")
            return
        student.balance -= payment
        print(f"Payment successful. Remaining balance: {student.balance}")

    def show_courses(self):
        if not self.courses:
            print("No courses added.")
            return
        print("Available Courses:")
        for course in self.courses:
            print(f"{course.course_id} - {course.name} (Fee: {course.fee})")

    # Main menu
    def show_menu(self):
        while True:
            print('+--------------------------------------------------------+')
            print('|         UNIVERSITY OF THE COMMONWEALTH CARIBBEAN       |')
            print('|          DEPARTMENT OF INFORMATION TECHNOLOGY          |')
            print('|                                                        |')
            print('|         COURSE REGISTRATION AND STUDENT PORTAL         |')
            print('|                                                        |')
            print('|    1. Register Student and Manage Details              |')
            print('|    2. Add Courses                                      |')
            print('|    3. Student Course Enrollment                        |')
            print('|    4. Make Payment                                     |')
            print('|    5. View Enrolled Students                           |')
            print('|    6. View Courses                                     |')
            print('|    Q. Exit                                             |')
            print('+--------------------------------------------------------+')
            option = input("Enter a selection [1-6 or Q]: ").strip().lower()
            if option == '1':
                self.register_student()
            elif option == '2':
                self.add_course()
            elif option == '3':
                self.enroll_in_course()
            elif option == '4':
                self.calculate_payment()
            elif option == '5':
                self.show_registered_students()
            elif option == '6':
                self.show_courses()
            elif option == 'q':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    system = RegistrationSystem()
    system.show_menu()
