import os
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
        
    with open("courses.txt", "r") as COURSES_INFO:
        print(COURSES_INFO.read())

# COURSE ENROLLMENT CODE 
def course_enrollment(student_ID, course_ID):
    '''FUNCTION:    To allow student to enroll in a course using their student ID, and course ID they want to enroll in. Also displays the enrolment date'''
    dateToday = datetime.datetime.now()
    enrolled = False
    
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

    with open("enrollment.txt", "a") as ENROLLMENT_INFO:
        ENROLLMENT_INFO.write(f"Student ID: {student_ID}, ")
        ENROLLMENT_INFO.write(f"Course ID: {course_ID}, ")
        ENROLLMENT_INFO.write(f"Enrollment Date: {dateToday.strftime("%d %B %Y")} \n")  # date format: dateNumber monthName year

# CODE TO DROP COURSE
def course_drop(student_ID, course_ID):
    ''' Function: To ask user to enter student id and course id that needs to be dropped from a course'''
    student_removed = False

    with open("enrollment.txt", "r") as ENROLLMENT_INFO:
        record_line = ENROLLMENT_INFO.readlines() #each line is now stored in record_line
        # print(record_line), This was just for me to see. delete before submitting
    
    with open("enrollment.txt", "w") as ENROLLMENT_INFO:
        for records in record_line: 
            if student_ID in records and course_ID in records: #if studentid and courseid in records, it deletes it, if not it skips and re-write record
                student_removed = True
                continue
            ENROLLMENT_INFO.write(records)
    
    if student_removed:
        print(f"Student {student_ID} was dropped from {course_ID}. Seat availability is being updated. ")
        
        with open("courses.txt", "r") as COURSES_INFO:
            course_lines = COURSES_INFO.readlines()
            
        with open("courses.txt", "w") as COURSES_INFO:
            for element in course_lines:
                if course_ID in element:
                    element_parts = element.strip().split(", ") # breaks course_lines info ["element 1: ", "element 2: ", "element 3: "]
                    available_seats = int(element_parts[2].split(": ")[1]) + 1 # calls index 2 and splits ["element 3: "] into ["element 3: ", "(data)"]. turns index 1 into an int and +1 since student dropped course
                    element = f"Course ID: {course_ID}, {element_parts[1]}, Avaliable Seats: {available_seats}\n"
                COURSES_INFO.write(element)
        print("You have successfully dropped the course")

    else:
        print("Enrollment record not found")

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

    match userInput:
        case 1: # Adding new student

            # To prevent the user from inputting the wrong student id format
            while True:
                student_ID = input("Please enter your student ID (e.g. 23132426): ") #converted to int later or else the try catch wouldnt work

                try:
                    student_ID = int(student_ID) 
                    if len(str(student_ID)) <= 8: #len cannot be int() so its converted to str()
                        break
                    else:
                        print("Ensure your student ID is less than 8 digits (e.g. 23132426): ")

                except ValueError:
                    print("Error! Enter a proper student ID")
            
            student_name = input("Please enter your name (e.g John Doe): ")
            
            #So if the student_contact is in int() the only format possible is "0161234567"
            while True:
                try:
                    student_contact = int(input("Please enter your phone number (e.g. 0161234567): "))
                    break
                except ValueError:
                    print("Error: enter a proper phone number! ")
                    
            adding_new_student(student_ID, student_name,student_contact)

            print(f"\nNew student added! Student ID: {student_ID}, Student Name: {student_name}, Contact Number: {student_contact}\n")
            
            while True:
                try:
                    userInput = input("Do you want to see the list of students? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("students.txt", "r") as STUDENT_INFO:
                            print(STUDENT_INFO.read())
                            break
                except:
                    print("ERROR! Enter a valid input please. ")
                    
        case 2: # To make a new course
            
            # To prevent the user from inputting the wrong courseid format
            while True:
                course_ID = input("Please input the course ID (e.g. CSC1024): ").upper() # not int(input()) cause course can be acronym
                if len(course_ID) <= 10:
                    break
                else:
                    print("Enter a proper course ID: ")   

            course_name = input("Please input course name (e.g. Programming Principles): ")

            while True:
                try:
                    available_seats = int(input("Please input seats available for the course (e.g. 30): ")) 
                    break      
                except ValueError:
                    print("Error: enter a proper number! ")

            adding_new_course(course_ID, course_name, available_seats)  

            print(f"New course added! Course ID: {course_ID}, Course Name: {course_name}, Available Seats: {available_seats}")
            
            while True:
                try:
                    userInput = input("Do you want to see the list of courses? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("courses.txt", "r") as COURSES_INFO:
                            print(COURSES_INFO.read())
                            break
                except:
                    print("ERROR! Enter a valid input please. ")
     
        case 3: # Enroll a student in a course
            # Display courses available 
            while True:
                student_ID = input("Please enter your student ID (e.g. 23132426): ") #converted to int later or else the try catch wouldnt work

                try:
                    student_ID = int(student_ID) 
                    if len(str(student_ID)) <= 8: #len cannot be int() so its converted to str()
                        break
                    else:
                        print("Enter a proper student ID (e.g. 23132426): ")

                except ValueError:
                    print("Error! enter a proper student ID")
                                                
            while True:
                course_ID = input("Please input the course ID (e.g. CSC1024): ").upper() # not int(input()) cause course can be acronym
                if len(course_ID) <= 10:
                    break
                else:
                    print("Enter a proper course ID: ") # Can't be int() because have initials of courses at the start
           
            course_enrollment(student_ID, course_ID)
            
            print(f"New student enrolled! Student ID: {student_ID}, Course ID: {course_ID}")
            
            while True:
                try:
                    userInput = input("Do you want to see the list of enrolled students? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("enrollment.txt", "r") as ENROLLMENT_INFO:
                            print(ENROLLMENT_INFO.read())
                            break
                except:
                    print("ERROR! Enter a valid input please. ")

        case 4: # Drop a course
            
            while True:
                student_ID = input("Please enter your student ID (e.g. 23132426): ") #converted to int later or else the try catch wouldnt work

                try:
                    student_ID = int(student_ID) 
                    if len(str(student_ID)) <= 8: #len cannot be int() so its converted to str()
                        break
                    else:
                        print("Enter a proper student ID (e.g. 23132426): ")

                except ValueError:
                    print("Error! enter a proper student ID")
                    
            while True:
                course_ID = input("Please input the course ID (e.g. CSC1024): ").upper() # not int(input()) cause course can be acronym
                if len(course_ID) <= 10:
                    break
                else:
                    print("Enter a proper course ID: ")
            
            course_drop(student_ID,course_ID)
  
        case 5: # View courses available and space left
            if os.path.exist("courses.txt"):
                with open("courses.txt", "r") as COURSES_INFO:
                    print(f"\n{COURSES_INFO.read()}\n")
            else:
                print("Error! File not found. ")
            
        case 6: # View all students and information
            if os.path.exist("students.txt"):
                with open("students.txt", "r") as STUDENT_INFO:
                    print(f"\n{STUDENT_INFO.read()}\n")
            else:
                print("Error! File not found. ")

        case 7:
            break

        case _:
            print("Invalid Choice. Try Again")