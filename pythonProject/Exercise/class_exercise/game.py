def Odd_number(x):
    return x%2!=0
numbers= [n for n in range(10)]
print(numbers)
print(len(numbers))
odd=[]

for i in range(len(numbers)):
    if Odd_number(numbers[i]):
        odd.append(i)
numbers = odd
print(numbers)