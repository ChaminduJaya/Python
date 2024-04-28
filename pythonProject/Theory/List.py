
marks=[23,67,78,'90',67] #Ordered collection and mutable
print(marks)
print(type(marks))
print(marks[2])
#print(marks[7])
print(len(marks))
marks[2]=99
#marks[7]=12 IndexError: list assignment index out of range
print(marks)

student=['cham','sona','chathu','disa']
print(student)
student[2]=78
print(student)
print(student+marks)
print(student.index('sona'))
print(marks.index(67,0,2))
print(marks.count(67))
print(marks.pop())#print only removing number
marks.pop()#remove last number from List
print(marks)
marks.pop(1)
print(marks)
student.remove('sona')
print('sona remove',student)
marks.append(3)
print(marks)
marks.extend([56,76])
print(marks)
print(marks+[98,99])
marks.insert(2,45)
print(marks)
marks2 =marks.copy()
print(marks2)
marks.reverse()
print(marks)
marks2.clear()#There is a emptry list
print(marks2,len(marks2))
del(marks2)#delete the List. now there are not at least empty list
#print(marks2)

print(len(marks))
#marks[6]=10 index out of range
print(99 in marks)
print(marks.count('90'))
lamai=['dad','wfwf','qwdeq']
lamai=' '.join(lamai)
print(lamai)
print(type(lamai))

hlo=[2,8,4,5,5]
#print(hlo.sort())#none
hlo.sort()
print(hlo)#Ascending order
hlo.reverse()
print(hlo)#descending order
hlo=[2,8,4,5,5]
hello=sorted(hlo)
print('hlo= ',hlo,'hello =',hello)
print('gh',hlo)


print(hlo[2:4])
print(hlo[::-1])
print(hlo[::2])
lk=hlo[::2]
print('hlo = ',hlo,' lk = ',lk)
hlo=[4,7,3,6]
print(max(hlo))
print(min(hlo))
print(sum(hlo))
fruit=['banana','apple','Apple','apples']
fruit.sort()# lexicographic order (alphabetical order)
print(fruit)
print(max(fruit))
#CP=[7,9,'gr','sfrqw'] #cant compare str and int
#CP.sort()
#print(CP)
CP=['7','9','gr','sfrqw']
CP.sort()
print(CP)
set_1={1,2,3}
tuple_1=(1,2,3)
print(list(set_1))
print(list(tuple_1))