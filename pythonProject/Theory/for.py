
LIST={1,2,3,10,78}
for x in LIST :
    print(x)
dic = [('cham',90),('sadun',89),('nuwan',86)]
for i in dic:
    print(i)
for i,j in dic:
    print(i,j)
for i in range(7):
    print(i)
for i in range(2,7):
    print(i)
for i in range(2,10,2):
    print('hi',i)
for i in range(10,2,-2):
    print('hi',i)

filtered_list = {item for item in LIST if item>10}
print(filtered_list)
filtered_elements = filter(lambda x: x > 10, LIST)
student=[2,'4','grege',6]
filtered_numbers = list(filter(lambda x: isinstance(x, (int, float)),student))
filtered_number= { x for x in student if isinstance(x,int)}
print(filtered_numbers)
print(list(filtered_elements))

squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
squared_numbers_tuple = tuple(x**2 for x in range(1, 6))
print(squared_numbers_tuple)  # Output: (1, 4, 9, 16, 25)
unique_squares = {x**2 for x in range(1, 6)}
print(unique_squares)  # Output: {1, 4, 9, 16, 25}
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

from array import array
my_array = array('i', [1, -2, 0])
array2 = array('I',[1,0,6])
array3 = array('f',[1.3,0,6.6])
array4 = array('d',[1.7,0,6])
print(my_array,array,array2,array4,array3)
print(array3[2])
array3.append(1.7)

'''
"i": Signed integer (platform-dependent size, often 4 bytes on most systems). posive and negative
"I": Unsigned integer (platform-dependent size, often 4 bytes on most systems).zero and positive
"f": Single-precision floating-point number (4 bytes).
"d": Double-precision floating-point number (8 bytes).

for i in List:#when i=3,(i=4 doesnt change like java)
    print(i)#3,4
    if i==3 :
        i-=1
        print(i) #print 2 .
for i in range(6):#when i=3,(i=4 doesnt change like java)
    print(i)#3,4
    if i==3 :
        i-=1
        print(i) #print 2 . 



nums = [12,16,18,21,29]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('not found')

num=10

for i in range(2,num):
    if num % i == 0:
        print ('not a prime')
        break
else :
    print ('prime')
'''