STUDENTS_INFO = "students.txt"
COURSES_INFO = "courses.txt"
ENROLLMENT_INFO = "enrollment.txt"

# STUDENT CODE
def adding_new_student(student_ID, student_name, student_contact):
    
    '''
    Function: To allow new students to add their student id, name and phone number
              Also clearly displays which is student ID, student name and student contact number in the .txt file
    '''

    with open("students.txt", "a") as STUDENTS_INFO:
        STUDENTS_INFO.write("Student ID: " + student_ID + ", ")
        STUDENTS_INFO.write("Student Name: " + student_name + ", ")
        STUDENTS_INFO.write("Student Contact Number: " + student_contact + "\n")

    # with open("students.txt", "r") as STUDENTS_INFO:
    #     print(STUDENTS_INFO.read())

    # return student_ID, student_name, student_contact

#COURSES CODE

# ENROLLMENT CODE

# ASKING USER RESPONSE CODE
while True:

    print("Welcome to the course enrollment program!")
    print("1. Add a new student")
    print("2. Add a new course")
    print("3. Enroll a student in a course")
    print("4. Enrol in a course")
    print("5. View available courses and space left")
    print("6. View all students")
    print("7. Exit")

    try:
        userInput = int(input("Enter a number: \n"))
    except:
        print("Please enter a number only: ")
        continue

        # replace all print statements with a function class from either student code, courses code or enrollment code
    match userInput:
        case 1: #adding new student
            student_ID = input("Please enter your student ID: ")
            student_name = input("Please enter your name: ")
            student_contact = input("Please enter your phone number: ")

            adding_new_student(student_ID, student_name,student_contact)

        case 2:
            print("im sad")
        case 3:
            print("me")
        case 4:
            print("me")      
        case 5:
            print("me")
        case 6:
            print("me")
        case 7:
            break
        case _:
            print("Invalid Choice. Try Again")
        
