'''import os.path
import pathlib

test_info = "C:/Users/harii/OneDrive - Sunway Education Group/Programming Coursework Year 1 Sem 1/thisistest.txt"
enroll_info = "C:/Users/harii/OneDrive - Sunway Education Group/Programming Coursework Year 1 Sem 1/enrollment.txt"
path = pathlib.Path(enroll_info)
if path.is_file():
    print("FOUND")
else:
    print("NOT FOUND!")

# with open("tempfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# with open("tempfile.txt", "a") as f:
#     f.write("\nBello")

# with open("tempfile.txt", "r") as f:
#     print(f.read())
'''
import datetime

dateToday = datetime.datetime.now()

print(f"Enrolment Date: {dateToday.strftime("%d %B %Y")} \n")

