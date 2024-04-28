
file=['chami','nuwan','sadun','chami','sadun','nipun']
print(f'Your memory is full.\nThere are these files.\n {file}')
duplicate= len(file)-len(set(file))
print(f'There are {duplicate} duplicate files.',end='')
delete=input('Do you want to delete duplicate files?(yes/no)\n ').lower()
print(delete)
if delete=='yes':
    print(list(set(file)))
elif delete == 'no':
    print('Ok')
else:
    print('please enter only yes or no')