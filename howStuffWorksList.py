# make sure file path use / not \
'''with open("C:/Users/Janice Lee/Desktop/1 Assignments/studentInfo.txt", 'r') as f:
    content = f.read()
    print(content)'''
    
# datetime to show date
import datetime
x = datetime.datetime.now()
print(x.strftime("%d %B %Y"))