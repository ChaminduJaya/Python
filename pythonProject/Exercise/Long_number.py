num = input('Enter number: ')
if num.isdigit():
    if len(num)<10 :
        if ',' not in num:
            coma = int((len(num)-1)/3)
            if coma==2:
                no=[num[:-6],num[-6:-3],num[-3:]]
                print(','.join(no))
            elif coma == 1:
                no = [ num[:-3], num[-3:]]
                print(','.join(no))
            else:
                print(num)

    else:
        print('Enter only less than 10 digit number')
else:
    print('Use only digits')