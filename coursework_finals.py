
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
def adding_new_course(course_ID, course_name, available_seats, total_students):
    ''' Function:   To allow new courses to be added with their course ID, course name and available seats for the course
                    Also clearly displays the courses and their information '''

    with open("courses.txt", "a") as COURSES_INFO: # writes the courses name in the textfile
        COURSES_INFO.write(f"Course ID: {course_ID}, ")
        COURSES_INFO.write(f"Course Name: {course_name}, ")
        COURSES_INFO.write(f"Available Seats: {available_seats}, ")
        COURSES_INFO.write(f"Total students in course: {total_students} \n")
        
    # with open("courses.txt", "r") as COURSES_INFO:        # shows the courses, for testing purposes
    #     print(COURSES_INFO.read())


# COURSE ENROLLMENT CODE 
def course_enrollment(student_ID, course_ID):
    '''FUNCTION:    To allow student to enroll in a course using their student ID, and course ID they want to enroll in
                    Also displays the enrolment date'''
                                                                                                        # either i forgo the total_students and just enroll student in regardless   
    dateToday = datetime.datetime.now()

    with open("courses.txt", "r") as ENROLLMENT_INFO:           # AAUGHHHHH ITS NOT WORKING
         #if total_students < available_seats:                   # there is probably a better method for this but i cant think of it rn
                #course_enrollment(student_ID, course_ID)        # What im trying to do: Check whether total_students is less than than available_seats (whether there's still availability in course)
        total_students += 1                                                #   , if yes got space then add student info and course info (and date) into enrolment.txt file                      
    with open("courses.txt", "a") as ENROLLMENT_INFO:                      #, and total_students counter + 1 / available_seats - 1
        ENROLLMENT_INFO.write(f"Student ID: {student_ID}, ")
        ENROLLMENT_INFO.write(f"Course ID: {course_ID}, ")
        ENROLLMENT_INFO.write(f"Enrollment Date: {dateToday.strftime("%d %B %Y")} \n")  # date format: dateNumber monthName year

    with open("enrollment.txt","r") as ENROLLMENT_INFO:         # these two lines for testing purposes, show enrollment info
        print(ENROLLMENT_INFO.read())


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
        case 1: #adding new student
            student_ID = input("Please enter your student ID: ") # not an int(input()) because the student ID could contain Letters for different departments
            student_name = input("Please enter your name: ")
            student_contact = int(input("Please enter your phone number: "))

            print("New student added.")
            adding_new_student(student_ID, student_name,student_contact)

        case 2: #to make a new course
            course_ID = input("Please input the course ID: ").upper() # not int(input()) cause course can be acronym
            course_name = input("Please input course name: ")
            available_seats = int(input("Please input available seats for the course: "))
            total_students = 0

            print("New course added >>")
            print(f"New Course: {course_ID}, Course Name: {course_name}, Total Available Seats: {available_seats}")   
            adding_new_course(course_ID, course_name, available_seats, total_students)  
        
        case 3: #Enroll a student in a course                                               # <<<< case 3 incomplete, to be fixed. Maybe also show all the courses before prompting for courseID
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
                print(f"\n{COURSES_INFO.read()}")
            

        case 6: # View all students and information
            with open("students.txt", "r") as STUDENT_INFO:
                print(f"\n{STUDENT_INFO.read()}")

        case 7:
            break

        case _:
            print("Invalid Choice. Try Again")
        
        
