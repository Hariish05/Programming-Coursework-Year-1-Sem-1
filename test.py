'''STUDENTS_INFO = "students.txt"
COURSES_INFO = "courses.txt"
ENROLLMENT_INFO = "enrollment.txt"'''

# STUDENT CODE

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
        case 1: 
            print("hi")
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
            print("me")
        case _:
            print("Invalid Choice. Try Again")
        



# HI This is a test