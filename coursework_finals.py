import os
import datetime

STUDENTS_INFO = "students.txt"
COURSES_INFO = "courses.txt"
ENROLLMENT_INFO = "enrollment.txt"

# STUDENT CODE
def adding_new_student(student_ID, student_name, student_contact):
    ''' Function: To allow new students to add their student ID, name and phone number '''

    with open("students.txt", "a") as STUDENTS_INFO:
        STUDENTS_INFO.write(f"Student ID: {student_ID}, ")
        STUDENTS_INFO.write(f"Student Name: {student_name}, ")
        STUDENTS_INFO.write(f"Student Contact Number: 0{student_contact} \n")

# COURSES CODE
def adding_new_course(course_ID, course_name, available_seats):
    ''' Function: To allow new courses to be added with their course ID, course name and available seats for the course. Also clearly displays the courses and their information '''

    with open("courses.txt", "a") as COURSES_INFO: 
        # writes the courses name in the textfile
        COURSES_INFO.write(f"Course ID: {course_ID}, ")
        COURSES_INFO.write(f"Course Name: {course_name}, ")
        COURSES_INFO.write(f"Available Seats: {available_seats}\n")

# COURSE ENROLLMENT CODE 
def course_enrollment(student_ID, course_ID):
    '''FUNCTION: To allow student to enroll in a course using their student ID, and course ID they want to enroll in. Also displays the enrolment date'''
    
    dateToday = datetime.datetime.now()
        
    # Read available courses
    enrolled = False
    course_exist = False
    with open("courses.txt", "r") as COURSES_INFO:
        # reads contents of the file and saves it to a variable, this is so it can be later added back into the text file
        lines = COURSES_INFO.readlines()

    with open("courses.txt", "w") as COURSES_INFO:
    # "w" will overwrite the existing contents in the text file
        for line in lines:
            if course_ID in line:
                course_exist = True
                parts = line.strip().split(", ")        
                # splits each line into 3 parts (separated by ",") = so like a list with 3 indexes > ["courseID info", "courseName", "seatInfo"]
                available_seats = int(parts[2].split(": ")[1])      
                # in part[2] (third index: seatInfo) = splits into two smaller parts (separated by ":") and defines available_seats as the integer in the 2nd index (smallerPart[1])

                if available_seats > 0:        
                    # if there is still seats available, -1 off the total available seats and add student and course info into enrollment.txt
                    available_seats -= 1
                    enrolled = True
                    print(f"Enrolling student {student_ID} in course {course_ID}")
                    
                    # append enrollment info into "enrollment.txt" file
                    with open("enrollment.txt", "a") as ENROLLMENT_INFO:        
                        ENROLLMENT_INFO.write(f"Student ID: {student_ID}, Course ID: {course_ID}, Enrollment Date: {dateToday.strftime("%d %B %Y")}\n")
                        # dateToday.strftime("%d %B %Y") >> strftime: returns the string representation of the date or time object; creates today's date in the format "dd mmmm yyyy"
                    print(f"\nNew student enrolled! Student ID: {student_ID}, Course ID: {course_ID}\n")
                
                else:
                    print("Course is full. Enrollment failed.")

                # gets the second element from the parts list, splits it at the : , and returns the part after the colon
                line = f"Course ID: {course_ID}, Course Name: {parts[1].split(': ')[1]}, Available Seats: {available_seats}\n"
            # this is to update course_info with the new updated available_seat total
            COURSES_INFO.write(line)      
        
        # error messages if course is full or if course ID does not exist in "courses.txt" file
        if not enrolled:
            print("No available seats.\n")
        elif not course_exist:
            print(f"Course {course_ID} does not exist.\n")

# CODE TO DROP COURSE
def course_drop(student_ID, course_ID):
    ''' Function: To ask user to enter student id and course id that needs to be dropped from a course'''
    
    student_removed = False

    with open("enrollment.txt", "r") as ENROLLMENT_INFO:
        record_line = ENROLLMENT_INFO.readlines() 
        # each line is now stored in record_line
    
    with open("enrollment.txt", "w") as ENROLLMENT_INFO:
        for records in record_line: 
            if student_ID in records and course_ID in records: #if studentID and courseID in records, it deletes it, if not it skips and re-write record
                student_removed = True
                continue
            ENROLLMENT_INFO.write(records)
    
    # if student has been successfully dropped from course, updates total available_seats in 'courses.txt' file accordingly
    if student_removed:
        print(f"\nStudent {student_ID} was dropped from {course_ID}. Seat availability is being updated.")
        
        with open("courses.txt", "r") as COURSES_INFO:
            course_lines = COURSES_INFO.readlines()
            
        with open("courses.txt", "w") as COURSES_INFO:
            for element in course_lines:
                if course_ID in element:
                    element_parts = element.strip().split(", ") 
                    # breaks course_lines info ["element 1: ", "element 2: ", "element 3: "]
                    available_seats = int(element_parts[2].split(": ")[1]) + 1 
                    # calls index 2 and splits ["element 3: "] into ["element 3: ", "(data)"]. turns index 1 into an int and +1 since student dropped course
                    element = f"Course ID: {course_ID}, {element_parts[1]}, Available Seats: {available_seats}\n"
                COURSES_INFO.write(element)
        print("\nYou have successfully dropped the course\n")

    else:
        print("\nEnrollment record not found\n")

# ASKING USER RESPONSE CODE
while True:

    print("Welcome to the course enrollment program!")
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
                try:
                    student_ID = int(input("Please enter your student ID (e.g. 23132426): ")) 
                    # converted to int later or else the try catch wouldnt work
                    student_ID = str(student_ID) 
                    if len(student_ID) > 8 or int(student_ID) < 0:
                        print("Ensure your student ID contains digits and is less than 8 digits (e.g. 23132426)")
                    else:
                        break
                except ValueError:
                    print("Error! Enter a proper student ID")
            
            student_name = input("Please enter your name (e.g John Doe): ")
            
            #So if the student_contact is in int() the only format possible is "0161234567"
            while True:
                try:
                    student_contact = int(input("Please enter your phone number (e.g. 0161234567): "))
                    if student_contact < 0:
                        print("Enter a proper phone number! ")
                    else:
                        break
                except ValueError:
                    print("Error: Enter a proper phone number! ")
                    
            # calls adding_new_student function
            adding_new_student(student_ID, student_name,student_contact)

            print(f"\nNew student added! Student ID: {student_ID}, Student Name: {student_name}, Contact Number: 0{student_contact}\n")
            
            while True:
                try:
                    userInput = input("Do you want to see the list of students? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("students.txt", "r") as STUDENT_INFO:
                            print(STUDENT_INFO.read())
                            break
                    elif userInput == "N":
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
                    print("Enter a course ID less than 10 characters: ")   

            course_name = input("Please input course name (e.g. Programming Principles): ")

            while True:
                try:
                    available_seats = int(input("Please input seats available for the course (e.g. 30): "))
                    if available_seats < 0:
                        print("Error: Do not enter seats less than 0! ")
                    else:
                        break      
                except ValueError:
                    print("Error: Enter a proper number! ")

            # calls adding_new_course function
            adding_new_course(course_ID, course_name, available_seats)  

            print(f"\nNew course added! Course ID: {course_ID}, Course Name: {course_name}, Available Seats: {available_seats}\n")
            
            while True:
                try:
                    userInput = input("Do you want to see the list of courses? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("courses.txt", "r") as COURSES_INFO:
                            print(COURSES_INFO.read())
                            break
                    elif userInput == "N":
                        break
                except:
                    print("ERROR! Enter a valid input please. ")
     
        case 3: # Enroll a student in a course
            # Display courses available 
            while True:
                try:
                    userInput = input("Do you want to see the list of courses? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("courses.txt", "r") as COURSES_INFO:
                            print(COURSES_INFO.read())
                            break
                    elif userInput == "N":
                        break
                except:
                    print("ERROR! Enter a valid input please. ")
            
            while True:
                try:
                    student_ID = int(input("Please enter your student ID (e.g. 23132426): ")) # converted to int later or else the try catch wouldnt work
                    student_ID = str(student_ID) 
                    if len(student_ID) > 8 or int(student_ID) < 0:
                        print("Ensure your student ID contains digits and is less than 8 digits (e.g. 23132426)")
                    else:
                        break
                except ValueError:
                    print("Error! Enter a proper student ID")
                                                
            while True:
                course_ID = input("Please input the course ID (e.g. CSC1024): ").upper() # not int(input()) cause course can be acronym
                if len(course_ID) <= 10:
                    break
                else:
                    print("Enter a proper course ID ") 
                    # Can't be int() because have initials of courses at the start
           
            # calls course_enrollment function
            course_enrollment(student_ID, course_ID)
            
            while True:
                try:
                    userInput = input("Do you want to see the list of enrolled students? (Y/N): ").upper()
                    if userInput == "Y":
                        with open("enrollment.txt", "r") as ENROLLMENT_INFO:
                            print(ENROLLMENT_INFO.read())
                            break
                    elif userInput == "N":
                        break
                except:
                    print("ERROR! Enter a valid input please. ")

        case 4: # Drop a course
            
            while True:
                try:
                    student_ID = int(input("Please enter your student ID (e.g. 23132426): ")) # converted to int later or else the try catch wouldnt work
                    student_ID = str(student_ID) 
                    if len(student_ID) > 8 or int(student_ID) < 0:
                        print("Ensure your student ID contains digits and is less than 8 digits (e.g. 23132426)")
                    else:
                        break
                except ValueError:
                    print("Error! Enter a proper student ID")
                    
            while True:
                course_ID = input("Please input the course ID (e.g. CSC1024): ").upper() # not int(input()) cause course can be acronym
                if len(course_ID) <= 10:
                    break
                else:
                    print("Enter a proper course ID: ")
            
            course_drop(student_ID,course_ID)
            
        case 5: # View courses available and space left
            # checks if file path for "courses.txt" exists in directory
            if os.path.exists("courses.txt"):
                with open("courses.txt", "r") as COURSES_INFO:
                    print(f"\n{COURSES_INFO.read()}\n")
            else:
                print("Error! File not found. ")
            
        case 6: # View all students and information
            # checks if file path for "students.txt" exists in directory
            if os.path.exists("students.txt"):
                with open("students.txt", "r") as STUDENT_INFO:
                    print(f"\n{STUDENT_INFO.read()}\n")
            else:
                print("Error! File not found. ")

        case 7:
            print("Program ended.")
            break

        case _:
            print("\nInvalid Choice. Try Again\n")