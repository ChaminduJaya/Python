dic= {'cham':89,
      'dil':90,
        'fgh':87,
      True:'tyhj',
      (7,8):True}
print(dic)
#print(dic[1])
print(dic['dil'])
#print(dic[90])
dic['cham']=56
print(dic)
dic[87]='sdfgh'
print(dic)
#dic.pop('chamiui')
print(dic.pop('cham'))
print(dic.keys())
print(dic.values())
print(dic.items())
print(type(dic))
print(type(dic.keys()))
print(type(dic.items()))
print(len(dic))
dic.clear()
print(dic)
del(dic)
#print(dic)

print('Hiiiii')
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Implicitly iterating over items using tuple unpacking
for i, j in my_dict.items():
    print(f'Key: {i}, Value: {j}')
