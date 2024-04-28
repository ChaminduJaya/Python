'''i=1
student=[]
while i<5:
    student.append(input(f'{i}. Enter  student name: '))
    i+=1
print(student)
student=[]
for j in range(1,5):
    student.append(input(f'{j}. Enter student name: '))
print(student)
'''
print('Enter name of student. after entered all name, enter -1')
student=[]
while True:
    name=input(f' Enter  student name: \n')
    '''
    if name=='-1':
        break
        '''
    if  name.isalpha():
        student.append(name)
        while True:
                ans= input('Do u want to add another name(yes/no):\n')
                if ans.lower()=='no':
                    break

                elif ans.lower()=='yes':
                    continue
                else:
                    print('please enter only yes or no')

                print(student)

    else:
        print('please enter only letters')
print(student)

print('_Enter marks of student_')
marks=[]
for i in range(len(student)):
    while True:
        value= input(f'Enter marks of {student[i]}: ')

        if value.isdigit():
            marks.append(int(value))
            break
        else:
            print('Invalid input')
print(marks)
for i in student:
    while True:
        value= input(f'Enter marks of {i}: ')

        if value.isdigit():
            marks.append(int(value))
            break
        else:
            print('Invalid input')
print(marks)
i=0
while i<len(student):
    value2 = input(f'Enter marks of {student[i]}: ')
    if value2.isdigit():
        marks.append(int(value))

    else:
        print('Invalid input')
        i-=1
    i+=1
print(marks)

