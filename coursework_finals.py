import datetime


STUDENTS_INFO = "students.txt"
COURSES_INFO = "courses.txt"
ENROLLMENT_INFO = "enrollment.txt"

# STUDENT CODE
def adding_new_student(student_ID, student_name, student_contact): 
    ''' Function: To allow new students to add their student id, name and phone number '''

    with open("students.txt", "a") as STUDENTS_INFO:
        STUDENTS_INFO.write(f"Student ID: {student_ID}, ")
        STUDENTS_INFO.write(f"Student Name: {student_name}, ")
        STUDENTS_INFO.write(f"Student Contact Number: {student_contact} \n")

#COURSES CODE
def adding_new_course(course_ID, course_name, max_seats):
    ''' Function:   To allow new courses to be added with their course ID, course name and maximum seats for the course
                    Also clearly displays the courses and their information '''

    with open("courses.txt", "a") as COURSES_INFO: # writes the courses name in the textfile
        COURSES_INFO.write(f"Course ID: {course_ID}, ")
        COURSES_INFO.write(f"Course Name: {course_name}, ")
        COURSES_INFO.write(f"Maximum seats: {max_seats} \n")

    #with open("courses.txt", "r") as COURSES_INFO: #shows the courses
        #print(COURSES_INFO.read())

# ENROLLMENT CODE
def course_enrollment():
    '''(TEXT)'''

    #with open("enrollment.txt", "a") as ENROLLMENT_INFO:
        

# ASKING USER RESPONSE CODE
while True:

    print("\nWelcome to the course enrollment program!")
    print("1. Add a new student")
    print("2. Add a new course")
    print("3. Enroll a student in a course")
    print("4. Drop a course")
    print("5. View available courses and space left")
    print("6. View all students and information")
    print("7. Exit")

    try:
        userInput = int(input("Enter a number: "))
    except:
        print("Please enter a number only: ")
        continue

        # replace all print statements with a function class from either student code, courses code or enrollment code
    match userInput:
        case 1: #adding new student
            student_ID = input("Please enter your student ID: ") # not an int(input()) because the student ID could contain Letters for different departments
            student_name = input("Please enter your name: ")
            student_contact = int(input("Please enter your phone number: "))

            print("New student added.")
            adding_new_student(student_ID, student_name,student_contact)

        case 2: #to make a new course
            course_ID = input("Please input the course ID: ").upper() # not int(input()) cause can have acronym for course
            course_name = input("Please input course name: ")
            max_seats = int(input("Please input maximum seats for the course: "))

            print("New course added >>")
            print(f"New Course: {course_ID}, Course Name: {course_name}, Maximum Seats: {max_seats}")   
            adding_new_course(course_ID, course_name, max_seats)  
        
        case 3: #Enroll a student in a course
            print("me")
        case 4: # Drop a course
            print("me")      
        case 5: # View courses available and space left
            print("me")
        case 6: # View all students and information
            print("me")
        case 7:
            break
        case _:
            print("Invalid Choice. Try Again")
        
