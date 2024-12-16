Author

Nzinga Lloyd

Date Created

December 15, 2024

Course

ITT103

GitHub Public URL to Code

[(https://github.com/Nzinga-coder2/Lloyd.Nzinga-Course_Registration-ITT103-F2024.py)]

Purpose of the Program

The Course Registration and Student Portal is a Python-based program designed to manage student registration, course enrollment, payment processing, and student deregistration for UCC. Additionally, the platform will enable administrative personnel to establish student profiles that contain the student's name, ID, and email address. Students can also use the program to track their balance owed to the institution and enroll in classes. Payments made by the student after enrollment must equal at least 40% of the remaining debt; else, an error message will appear.

It implements key Object-Oriented Programming (OOP) principles such as encapsulation, modular design, and abstraction to ensure maintainable and reusable code.

Features:

Register Students: Add new students with unique IDs, names, and email addresses.

Add Courses: Create new courses with unique IDs, names, and fees.

Enroll in Courses: Link students to courses and automatically update their outstanding balance.

Deregister Students: Remove a student from the system and all associated courses.

Make Payments: Process payments towards a student’s balance with a minimum threshold.

View Information:

View all registered students and their details.

View all available courses and their fees.

How to Run the Program

Requirements:

Python Version: The program requires Python 3.7 or later.

Instructions:

Clone or download the program files from the GitHub repository.

Navigate to the directory containing the program file (Lloyd.Nzinga-Course_Registration-ITT103-F2024.py).

Open a terminal or command prompt and run the program 

Follow the menu prompts to interact with the system.

Assumptions

Student IDs and Course IDs:

Both IDs are unique across the system and manually entered.

Email Validation:

Emails are expected to conform to standard email formatting rules.

Payment Threshold:

Payments must meet a minimum of 40% of the student’s outstanding balance.

Limitations

No Database Integration:

The system uses in-memory data storage and does not persist data between sessions.

Limited Input Validation:

User inputs like names or IDs are not heavily validated beyond uniqueness.

Concurrent Access:

The system does not support concurrent multi-user access.

Dependencies: 

The program uses the built-in re module for email validation, so no external libraries need to be installed.
