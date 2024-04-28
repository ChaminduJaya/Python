new=input('Do you already have another account(yes/no):')
if new.lower() == 'no':
    Email= input('Enter your email adress:')
   # print(Email.index('@',1,3))
   # print(Email.find('@',-10,-1))
   # print(Email[-10:-4])
    if(Email[-10:]=='@gmail.com' or Email[-10:]=='@yahoo.com' ):
        pw= input('Enter your password')
        if len(pw)>7 and pw.isalnum() and not pw.isspace():
            pw2=input('re-enter your password')
            if pw==pw2:
                print(f'Your {Email[-9:-4]} account is created')
            else:
                print('your password is incorrect')
        else:
            print('You must have to use at least 8 character and must not be every characters are letters ')

if new.lower() == 'yes':
   Email= input('Enter your email adress:')
   pw =input('Enter your password')

