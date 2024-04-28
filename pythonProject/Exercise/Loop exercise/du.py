#remove duplicate element and create new array
a=[2,3,4,3,2,6,7,8]
b=[]
for i in a:
    print(i,'first')
    if i not in b:
        b.append(i)
print(b)

i=0
while i<10:
    print(i*'*')
    i=i+1