import os.path
import pathlib

with open("students.txt", "r") as students_f:
    # print(students_f.read())
    # print(students_f.readline())
    student_lines = students_f.readline()
    # print(students_f.readlines())
    for line in student_lines:
        print(line)

# test_info = "C:/Users/harii/OneDrive - Sunway Education Group/Programming Coursework Year 1 Sem 1/thisistest.txt"
# enroll_info = "C:/Users/harii/OneDrive - Sunway Education Group/Programming Coursework Year 1 Sem 1/enrollment.txt"
# path = pathlib.Path(enroll_info)
# if path.is_file():
#     print("FOUND")
# else:
#     print("NOT FOUND!")

# # with open("tempfile.txt", "r") as f:
# #     content = f.read()
# #     print(content)

# # with open("tempfile.txt", "a") as f:
# #     f.write("\nBello")

# # with open("tempfile.txt", "r") as f:
# #     print(f.read())

# import datetime

# dateToday = datetime.datetime.now()

# print(f"Enrolment Date: {dateToday.strftime("%d %B %Y")} \n")'''



# seats = []  # 1 = occupied, 0 = available
# count = 0
# total_students = 0
# for count in range(200):
#     seats.append("0")
#     count+= 1

# available_seats = seats.count("0")
# print(available_seats)