name=('dsf',8,'frfr') #ordered collection and immutable-order and element.(normally use historical data)
print(type(name))
print(name)
print(name[0])
#name[0]='fdh'
print(name.index(8))
print(name.count(8))
print(name[::-1])
num=(6,8,9,5,6)
print('ydj',min(num))
print(sorted(num))
print(num)
num=(3,45,6)
name=(4,6,7)
print(num+name)
ds=[4,7,8]
#print(ds+name)
print(6 in num)

list_1=[1,2,3]
set_1={1,2,3}
print(tuple(list_1))
print(tuple(set_1))