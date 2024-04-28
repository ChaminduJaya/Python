
class shed:

    print('\t\t\t','_'*10 ,'Galle Shed', '_'*10)
    petrol_available ='not available'
    diesel_available ='not available'
    petrol_92_available ='not available'
    petrol_95_available = 'not available'
    auto_diesel_available = 'not available'
    super_diesel_available = 'not available'
    Price=0
    petrol_92_price_1L=0
    petrol_95_price_1L=0
    super_diesel_price_1L=0
    auto_diesel_price_1L=0
    Total_Liters=0
    diesel_price=0
    petrol_price=0
    petrol_litters=0
    diesel_litters=0

    petrol_92_volume=0
    petrol_95_volume=0
    super_diesel_volume=0
    auto_diesel_volume=0


    def cal_fuel_price(fuel_price_1L, fuel_volume):
        Total_fuel_price = int(fuel_price_1L) * int(fuel_volume)
        print(fuel_price_1L, fuel_volume)
        return Total_fuel_price



    def cal_fuel_Liters(fuel_price,fuel_price_1L):
        Litters =fuel_price/fuel_price_1L
        return Litters

    def print_price (petrol_price:0,diesel_price:0):
        petrol_price = str(petrol_price)
        diesel_price=str(diesel_price)
        print(' ' + '_' * 8, ' '.ljust(30), '_' * 8)
        print('|' + f' {petrol_price.zfill(5)}'.ljust(8) + '|' + 'Price'.center(30) + '|' + f' {diesel_price.zfill(5)}'.ljust(8) + '|')
        print('|' + '_' * 8 + '|' + ' '.ljust(30) + '|' + '_' * 8 + '|')

    def print_litters(petrol_litters:0,diesel_litters:0):
        petrol_litters=str(petrol_litters)
        diesel_litters=str(diesel_litters)
        print(' ' + '_' * 8, ' '.ljust(30), '_' * 8)
        print('|' + f' {petrol_litters.zfill(5)}'.ljust(8) + '|' + 'Litters'.center(30) + '|' + f' {diesel_litters.zfill(5)}'.ljust(8) + '|')
        print('|' + '_' * 8 + '|' + ' '.ljust(30) + '|' + '_' * 8 + '|')

    def requested_fuel_available(fuel_volume,required_litters):
        if fuel_volume>=required_litters :
            return "available"
        return "not available"
    def cal_new_fuel_volume(fuel_volume,released_litters):
        fuel_volume-=released_litters
        return fuel_volume


    @classmethod
    def fuel_available(cls):

        if cls.petrol_92_volume > 0:
            cls.petrol_92_available = 'available'

        if cls.petrol_95_volume > 0:
            cls.petrol_95_available = 'available'
        if cls.petrol_95_volume > 0 and cls.petrol_92_volume > 0 :
            cls.petrol_available = 'available'
        if cls.auto_diesel_volume > 0:
            cls.auto_diesel_available = 'available'
        if cls.super_diesel_volume > 0:
            cls.super_diesel_available= 'available'
        if cls.auto_diesel_volume > 0 and cls.super_diesel_volume > 0 :
            cls.diesel_available = 'available'


    while True:

        #fuel_available(petrol_92_volume,petrol_95_volume,auto_diesel_volume,super_diesel_volume,petrol_available,diesel_available,petrol_92_available,petrol_95_available,auto_diesel_available,super_diesel_available)

        point1_text = f'1).Petrol - {petrol_available}'.ljust(30)
        point2_text = f'2).Diesel - {diesel_available}'
        point3_text = f'3).Change Price'.ljust(30)
        point4_text = f'4).Tank fuel'

        print(f'{point1_text}{point2_text}\n{point3_text}{point4_text}\n')

        while True:
            Option=input('Chose a option: ')
            if Option.isdigit() :
                Option= int(Option)
                if Option<5:
                    if Option==1 or Option==2 :

                        if Option==1:
                            petrol_price = input('Price :')
                            if petrol_price.isdigit():
                                petrol_price=int(petrol_price)
                                print('Petrol'.center(50))
                                print('1). 92 Octane'.ljust(30,'_'))
                                print('2). 95 Octane'.ljust(30,'_'))
                                print('3).Exit\n')

                                while True:
                                    petrol_type=input('Chose a option: ')
                                    if petrol_type.isdigit():
                                        petrol_type = int(petrol_type)
                                        if petrol_type < 4:
                                            if petrol_type == 1:
                                                petrol_litters = cal_fuel_Liters(petrol_price, petrol_92_price_1L)
                                                Available = requested_fuel_available(petrol_92_volume, petrol_litters)

                                                print(Available)
                                                if Available=='available':
                                                    petrol_92_volume=cal_new_fuel_volume(petrol_92_volume,petrol_litters)
                                            elif petrol_type == 2:
                                                petrol_litters = cal_fuel_Liters(petrol_price, petrol_95_price_1L)
                                                Available = requested_fuel_available(petrol_95_volume, petrol_litters)
                                            #else:

                                            break
                                        else:
                                            print('Invalid number')
                                    else:
                                        print('Please use only digits')
                            else:
                                print('Please use only digits')


                        elif Option == 2:
                            diesel_price = input('Price :')
                            if diesel_price.isdigit():
                                diesel_price=int(diesel_price)
                                print('Diesel'.center(50))
                                print('1). Super Diesel'.ljust(30, '_'), f'{Available}')
                                print('2). Auto Diesel'.ljust(30, '_'), f'{Available}')
                                print('3).Exit\n')


                                while True:
                                    diesel_type = input('Chose a option: ')
                                    if diesel_type.isdigit():
                                        diesel_type = int(diesel_type)
                                        if diesel_type < 4:
                                            if diesel_type == 1:
                                                diesel_litters = cal_fuel_Liters(diesel_price,super_diesel_price_1L)
                                                Available = requested_fuel_available(super_diesel_volume,diesel_litters)
                                            elif diesel_type == 2:
                                                diesel_litters = cal_fuel_Liters(diesel_price,auto_diesel_price_1L)
                                                Available = requested_fuel_available(auto_diesel_volume, diesel_litters)
                                            #else:
                                            break
                                        else:
                                            print('Invalid number')
                                    else:
                                        print('Please use only digits')

                            else:
                                print('use only digits')
                        if Available == "available":
                            print_price(petrol_price, diesel_price)
                            print_litters(petrol_litters,diesel_litters)

                        else:
                            print('Sorry. There is no enough fuel')
                        break

                    if Option==3:
                        print("Please select a type of fuel:")
                        print('1). 92 Octane'.ljust(20), '2). 95 Octane')
                        print('3). Super Diesel'.ljust(20), '4). Auto Diesel')
                        print('5). Exit'.center(36))
                        Fuel_type = input('\nChose a option :')
                        if Fuel_type.isdigit():
                            Fuel_type = int(Fuel_type)
                            if Fuel_type < 6:
                                Fuel_price = input("Enter new price of 1L")
                                if Fuel_price.isdigit():
                                    Fuel_price=int(Fuel_price)
                                    if Fuel_type == 1:
                                        petrol_92_price_1L = Fuel_price
                                    elif Fuel_type == 2:
                                        petrol_95_price_1L = Fuel_price
                                    elif Fuel_type == 3:
                                        super_diesel_price_1L = Fuel_price
                                    elif Fuel_type == 4:
                                        auto_diesel_price_1L = Fuel_price
                                    # else:
                                else:
                                    print('use only digits')
                                break

                    if Option==4:
                        while True:
                            print("Please select a type of fuel:")
                            print('1). 92 Octane'.ljust(20),'2). 95 Octane')
                            print('3). Super Diesel'.ljust(20),'4). Auto Diesel')
                            print('5). Exit'.center(36))

                            Fuel_type=input('Chose a option :')
                            if Fuel_type.isdigit() :
                                Fuel_type=int(Fuel_type)
                                if Fuel_type < 6:
                                    Tank_Liter = input("What's the amount of Liter do you want to tank:")
                                    if Tank_Liter.isdigit():
                                        Tank_Liter=float(Tank_Liter)
                                        if Fuel_type==1:
                                            petrol_92_volume+=Tank_Liter
                                        elif Fuel_type==2:
                                            petrol_95_volume+=Tank_Liter
                                        elif Fuel_type==3:
                                            super_diesel_volume+=Tank_Liter
                                        elif Fuel_type==4:
                                            auto_diesel_volume+=Tank_Liter
                                        #else:
                                        break
                                    else:
                                        print('Use only digits')
                                else:
                                    print('Invalid number')
                            else:
                                print('Use only digits')
                    break
                else:
                    print('Invalid number')
            else :
                print('Please use only digits')

shed.fuel_available()

