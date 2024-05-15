def add(number):
    number*=number
    if number%5 == 0:
        print('return')
        return # retrn act as a break
    print('not return')

add(5)

def shehan(number):
    print('hi')
    return number*number

shehan(5)
y=shehan(10)

print(y)
x=add(6)
print(x)
