
student=[]
student.append(input("Enter 1st student name: "))
mark1=input("Enter 1st student marks: ")
student.append(input("Enter 2nd student name: "))
mark2=input("Enter 2nd student marks: ")
student.append(input("Enter 3rd student name: "))
mark3=input("Enter 3rd student marks: ")
marks=[mark1,mark2,mark3]
print(student[0]+'marks is'+marks[0])
print(student[1],'marks is',marks[1])
print(f'{student[2]} marks is {marks[2]}')