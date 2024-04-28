'''Name= input('enter your name: ')
Name=Name.upper()
print(Name)
Name= input('enter your name: ').lower().capitalize()
print(Name)
Name= input('enter your name: ').casefold() #casefold same as lower
print(Name)
Name= input('enter your name: ').swapcase()
print(Name) #cHAMINDU
print(Name[1].lower()) #h
print(Name)     #cHAMINDU
#Name[1]= Name[1].lower()
#Name[1]='d'
Name=input('Enter name: ') #Chaaamii
Name=Name.replace('a','z')
print(Name)  #Chzzzmii
Name=Name.replace('z','a',2)
print(Name)#Chaazmii
print('M' in Name)
'''
Name = 'chafg '
Name2 = 'cha#hgd'
print(Name.split())
print(Name2.split('#'))
print(Name[3].isspace())
print(Name.find('a'))
print(Name.find('z'))
print(Name.find('a',0))
print(Name.find('a',0,2))
print(Name.find('a',0,2))
print(Name.find('a',-1,-4))
Senten='I came to yoga'
print(Senten.replace(' ','#'))
print(Senten.replace(' ','#',2))
print(Senten.count('o'))
print(Senten.count('o',0,7))
print(Senten.removesuffix("a"))
print(Senten.removeprefix('I'))
print(Senten.removesuffix("yoga"))
print(Senten.__add__('ghghh'))
Name1 = 'chamindu'
Name2 = 'jayalath'
FullName = Name1+' '+ Name2
print(FullName)
print('c' in Name1[3:5])