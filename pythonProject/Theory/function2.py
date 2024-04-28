a=10
b=12
print(id(a))
def sth():
   # print (a)  cant take global
    global b
    print ('b',b)
    a=9
    x=globals()['a']
    print (id(x))

    print ('fun',x)
    globals()['a']=15
    print ('hi',x)
sth()
print('jolly' ,a)


def count(list):
    odd = 0
    even = 0
    for i in list:
        if i % 2 ==0 :
            even+=1
        else:
            odd+=1
    return odd,even

lst = [3,6,7,9,10,23,4,67,87,34]
odd,even = count(lst)
print ('odd',odd,'even',even)

#recrusion
import sys
sys.setrecursionlimit(2000)
print (sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print ('hello',i)
    greet()
greet()
