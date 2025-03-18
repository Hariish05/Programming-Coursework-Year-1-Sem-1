
import os.path
import pathlib
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


# COURSES CODE
def adding_new_course(course_ID, course_name, available_seats):
    ''' Function:   To allow new courses to be added with their course ID, course name and available seats for the course
                    Also clearly displays the courses and their information '''

    with open("courses.txt", "a") as COURSES_INFO: # writes the courses name in the textfile
        COURSES_INFO.write(f"Course ID: {course_ID}, ")
        COURSES_INFO.write(f"Course Name: {course_name}, ")
        COURSES_INFO.write(f"Available Seats: {available_seats}\n")


# COURSE ENROLLMENT CODE 
def course_enrollment(student_ID, course_ID):
    '''FUNCTION:    To allow student to enroll in a course using their student ID, and course ID they want to enroll in
                    Also displays the enrolment date'''
    
    dateToday = datetime.datetime.now()

    # Read available courses
    enrolled = False
    with open("courses.txt", "r") as COURSES_INFO:
        lines = COURSES_INFO.readlines()

    with open("courses.txt", "w") as COURSES_INFO:
        for line in lines:
            if course_ID in line:
                parts = line.strip().split(", ")        # splits each line into 3 parts (separated by ",") = so like a list with 3 indexes > ["courseID info", "courseName", "seatInfo"]
                available_seats = int(parts[2].split(": ")[1])      # in part[2] (third index: seatInfo) = splits into two smaller parts (separated by ":") and defines available_seats as the integer in the 2nd index (smallerPart[1])

                if available_seats > 0:        # if there is still seats available, -1 off the total available seats and add student and course info into enrollment.txt
                    available_seats -= 1
                    enrolled = True
                    print(f"Enrolling student {student_ID} in course {course_ID}")
                    with open("enrollment.txt", "a") as ENROLLMENT_INFO:        
                        ENROLLMENT_INFO.write(f"Student ID: {student_ID}, Course ID: {course_ID}, Enrollment Date: {dateToday.strftime("%d %B %Y")}\n")
                else:
                    print("Course is full. Enrollment failed.")

                line = f"Course ID: {course_ID}, Course Name: {parts[1].split(': ')[1]}, Available Seats: {available_seats}\n"
                
            COURSES_INFO.write(line)      # this is to update course_info with the new updated available_seat total

    if not enrolled:        # if courseID is wrong/non-existent display error message
        print("Course not found.")


# CODE TO DROP COURSE
def course_drop(student_ID, course_ID):
    ''' Function: To ask user to enter student id and course id that needs to be dropped from a course'''

    with open("enrollment.txt", "r") as ENROLLMENT_INFO:
        record_line = ENROLLMENT_INFO.readlines() #each line is now stored in record_line
        # print(record_line), This was just for me to see. delete before submitting
    
    with open("enrollment.txt", "w") as ENROLLMENT_INFO:
        for records in record_line: 
            if student_ID in records and course_ID in records: #if studentid and courseid in records, it deletes it, if not it skips and re-write record
                continue
            ENROLLMENT_INFO.write(records)


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
        case 1: # Adding new student
            student_ID = input("Please enter your student ID: ") # not an int(input()) because the student ID could contain Letters for different departments
            student_name = input("Please enter your name: ")
            student_contact = int(input("Please enter your phone number: "))

            print("\nNew student added:")
            print(f"Student ID: {student_ID}, Student Name: {student_name}")
            adding_new_student(student_ID, student_name,student_contact)

        case 2: # To make a new course
            course_ID = input("Please input the course ID: ").upper() # not int(input()) cause course can be acronym
            course_name = input("Please input course name: ")
            available_seats = int(input("Please input seats available for the course: "))       # ADD error-handling for this part

            print("\nNew course added: ")
            print(f"Course ID: {course_ID}, Course Name: {course_name}, Available Seats: {available_seats}")   
            adding_new_course(course_ID, course_name, available_seats)  
        
        case 3: # Enroll a student in a course   
            # display courses available                   
            student_ID = input("Please enter your student ID: ")                        
            course_ID = input("Please input the course ID you want to enrol in: ").upper()

            course_enrollment(student_ID, course_ID)
            
        case 4: # Drop a course
            student_ID = input("Please enter the student ID:")
            course_ID = input("Please enter the course ID: ").upper()

            course_drop(student_ID,course_ID)
            print("You have successfully dropped the course")
            
        case 5: # View courses available and space left
            with open("courses.txt", "r") as COURSES_INFO:
                print(f"\n{COURSES_INFO.read()}\n")
            

        case 6: # View all students and information
            with open("students.txt", "r") as STUDENT_INFO:
                print(f"\n{STUDENT_INFO.read()}\n")

        case 7:
            break

        case _:
            print("Invalid Choice. Try Again")
        
        
