def sum():
    print('sum')
def sum(x,y): # can't overload in same name method. when same name overriden happen.clearlest method will run
    print('no overloading',x,y)
sum('d',8)

def avg():
    x=9
    y=7
    return x
print(avg(),type(avg()))
def avg():
    x=9
    y=7
    return x,y
print(avg(),type(avg()))
def list():
    x=[2,2,2,2]
    y=8
    return x,y
print(list(),type(list()))#([2,2,2,2],8)
print(list()[0])
def cham():
    return None
print(cham(), type(cham()))
def suma():
    print('hi')
print(type(suma()),suma())
def rata(country:'Srl lanka'):
    print(country)
rata('norway')

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1, result2 = add_sub(7,9)
print(result1)


def update(x):
    x=8
    print (x)

a=10
update(a)
print (a)

def sum(a,b):
    c=a+b
    print (c)

# sum(4,7,8,9)  #sum() takes 2 positional arguments but 4 were given
def sum2(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum2(4,7,8,9)

def person (name, **data):
    print(name)
    for i,j in data.items() :
        print (i,j)

person('nuwan',age=28,city='Galle',TP=7185420)

