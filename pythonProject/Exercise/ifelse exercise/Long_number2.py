num=input('Enter long number (if You wish use coma: )')
if num.isdigit() :
    print('your data is entered')
elif num.isalpha() or num.isalnum() :
    print('please enter with digits')
else:
    if ',' in num :
        num= num.split(',')
        print(''.join(num))




