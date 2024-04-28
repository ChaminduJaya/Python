Price=input('Enter price: (with cent)')#String
if not Price.isalpha()  and not Price.isalnum():
   
    if '.' in Price :
        dot=Price.index('.')

        if len(Price[dot+1:])==2:
            print('Rupees:',Price[:dot],int(float(Price)))
            print('Cent:',Price[dot+1:])
        else:
            print('Cent must have only two digit')
    else :
        print('you must enter price with cent')

    if '.' in Price and Price[-3]=='.' :
            print('Rupees:', Price[:-3])
            print('Cent:', Price[-2:])
else:
    print('Please enter price in digits')