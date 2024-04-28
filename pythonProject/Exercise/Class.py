student={'cham','nipun','suyama','sadun','nuwan'}
count=len(student)
print(f'This is your student name: \n{student}')
change=input('Do u want to add or remove student from class(+,-): \n')
if change=='+':
    new= input('Enter name of new student: \n')
    if new.isalpha():
        student.add(new)
        if count<len(student):
            print(student)
        else:
            print(f'{new} name is already included')
    else:
        print('please enter only letters')
elif change=='-':
    new= input('Enter name of new student: \n')
    if new.isalpha():
        if new in student:
            student.remove(new)
            print(student)
        else:
            print(f'{new} is not included')
    else:
        print('please enter only letters')
else:
    print('Please enter only "+"or "-" ')
