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
#hellu
    if userInput == 1:
        #add new student function
        #make sure it goes into #STUDENTS CODE
    elif userInput == 2: ''' WHY IS IT RED AND SAYING ITS AN ERROR HELP SOS FFS'''
        #add new course function
        #make sure it goes into #COURSE CODE
    elif userInput == 3:
        #add a enroll student function
        #make sure it goes into #STUDENTS CODE
    elif userInput == 4:
        #add a drop course function
        #make sure it goes into #COURSE CODE
    elif userInput == 5:            
        #add a view courses function
        #make sure it goes into #COURSE CODE
    elif userInput == 6:
        #add view student function
        #make sure it goes into #STUDENTS CODE
    elif userInput == 7:
        print("Thank you for using the course enrollment program!")
        break