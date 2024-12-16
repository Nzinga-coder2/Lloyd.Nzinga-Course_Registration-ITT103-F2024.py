import re

class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        return True

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return True
        return False

class Student:
    def __init__(self, student_id, name, email, courses=None, balance=0):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = courses if courses else []
        self.balance = balance

    def enroll_in_course(self, course):
        self.courses.append(course)
        self.balance += course.fee

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            self.balance -= course.fee

class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def add_course(self):
        course_id = input("Enter Course ID: ")
        if any(course.course_id == course_id for course in self.courses):
            print(f"Error: Course ID {course_id} already exists.")
            return
        name = input("Enter Course Name: ")
        try:
            fee = float(input("Enter Course Fee: "))
        except ValueError:
            print("Error: Fee must be a valid number.")
            return
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
        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return
        student = Student(student_id, name, email)
        self.students[student_id] = student
        print(f"Student '{name}' successfully registered.")

    def deregister_student(self):
        student_id = input("Enter Student ID to Deregister: ")
        student = self.students.get(student_id)
        if not student:
            print("Error: Student not found.")
            return
        # Remove student from all enrolled courses
        for course in student.courses:
            course.remove_student(student)
        del self.students[student_id]
        print(f"Student '{student.name}' has been successfully deregistered.")

    def show_registered_students(self):
        print("Registered Students:")
        for student_id, student in self.students.items():
            print(f"{student_id} - {student.name} (Email: {student.email}) Balance: ${student.balance:.2f}")

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
        if course in student.courses:
            print(f"Error: Student is already enrolled in '{course.name}'.")
            return
        course.add_student(student)
        student.enroll_in_course(course)
        print(f"Student '{student.name}' enrolled in '{course.name}'. New Balance: ${student.balance:.2f}")

    def drop_course(self):
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
        if course not in student.courses:
            print(f"Error: Student is not enrolled in '{course.name}'.")
            return
        course.remove_student(student)
        student.drop_course(course)
        print(f"Student '{student.name}' dropped from '{course.name}'. New Balance: ${student.balance:.2f}")

    def calculate_payment(self):
        student_id = input("Enter Student ID: ")
        student = self.students.get(student_id)
        if not student:
            print("Error: Student not found.")
            return
        print(f"Outstanding Balance: ${student.balance:.2f}")
        try:
            payment = float(input("Enter Payment Amount: "))
        except ValueError:
            print("Error: Payment must be a valid number.")
            return
        if payment < 0.4 * student.balance:
            print("Error: Payment must be at least 40% of the outstanding balance.")
            return
        student.balance -= payment
        print(f"Payment successful. Remaining Balance: ${student.balance:.2f}")

    def show_courses(self):
        if not self.courses:
            print("No courses added.")
            return
        print("Available Courses:")
        for course in self.courses:
            print(f"{course.course_id} - {course.name} (Fee: ${course.fee:.2f})")

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
            print('|    4. Drop Course                                      |')
            print('|    5. Make Payment                                     |')
            print('|    6. View Enrolled Students                           |')
            print('|    7. View Courses                                     |')
            print('|    8. Deregister Student                               |')
            print('|    Q. Exit                                             |')
            print('+--------------------------------------------------------+')
            option = input("Enter a selection [1-8 or Q]: ").strip().lower()
            if option == '1':
                self.register_student()
            elif option == '2':
                self.add_course()
            elif option == '3':
                self.enroll_in_course()
            elif option == '4':
                self.drop_course()
            elif option == '5':
                self.calculate_payment()
            elif option == '6':
                self.show_registered_students()
            elif option == '7':
                self.show_courses()
            elif option == '8':
                self.deregister_student()
            elif option == 'q':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = RegistrationSystem()
    system.show_menu()
