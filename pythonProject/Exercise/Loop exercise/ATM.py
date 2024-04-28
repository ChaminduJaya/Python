print('Welcome to BoC bank')

Acc_Balance=0
while True:
    Acc_No=input('Enter your Account number:')
    if len(Acc_No)==8 and Acc_No.isdigit() :
        while True:
            pw= input('Enter pin number: \n')
            if len(pw)==4 and pw.isdigit():

                while (True):
                    ans=input('What do you want to do (withdraw/deposit):\n').lower()
                    if ans == "deposit" or ans =="withdraw":
                        while True:
                            trans= input(f'Enter your {ans} value:\n')
                            if trans.isdigit():
                                trans=int(trans)
                                if ans == "deposit":
                                    Acc_Balance= Acc_Balance+trans
                                    print(f"Your account balance is {Acc_Balance}")
                                    break
                                else:
                                    if Acc_Balance>=trans :
                                        Acc_Balance = Acc_Balance - trans
                                        print(f"Your account balance is {Acc_Balance}")
                                        break
                                    else:
                                        print(f"your account balance is {Acc_Balance } and it is not sufficient.")
                                        continue

                            else:
                                print('Use only digits')
                        another= input('Do you want to do another transaction?(yes/no)').lower()
                        if another =='no':
                            print('Thank you. Come again')
                            break

                    else:
                        print('please enter only that withdraw or deposit')
                break
            else:
                print("invalid password")
                continue
        break
    else:
        print("Invalid Account number")
        continue





