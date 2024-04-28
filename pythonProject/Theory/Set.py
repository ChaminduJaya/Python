name={4,6,8,9,2,2}#unordered collection with unique elements
print(type(name))
print(name)
print(name)
no={5,8,9,0}
print(no)
print(no)
print('max',max(no),'min=',min(no),'sum=:',sum(no))
#print(name[0:3])
bs={9,'dgh',6,'sdf','fgfhj',8,7,6,6}
print(bs)
#print(bs[1])
#bs[0]=8
bs.remove(6)
print(len(bs))
print('POP',bs.pop())# we used when we want remove element randomly
bs.pop()
print(bs)
bs.add(57)
print('shyjh',bs)
name={4,5,6,7}
bs={3,5,6,9,1}
#print(name+bs)
print(bs | name)
print('intersec',bs & name)
print(bs-name)
print(name-bs)
print(bs.intersection(name))
print(bs.union(name))
print(bs.difference(name))
print(name.difference(bs))
#print(bs+name)
df=[5,6,7]
#print(df+name)
print(8 in bs)