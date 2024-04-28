#Q 1.1
while True:
    Today=input('Date(year/month/date) :')

    if  Today.count('/') ==2:

        Today_List = Today.split('/')
        Today_long = ''.join(Today_List)

        if Today_long.isdigit():
                date = int(Today_List[2])
                month = int(Today_List[1])
                year = int(Today_List[0])
                if (len(str(year))==4 and month<=12 and date<=31):
                    Today_List.reverse()
                    Today='/'.join(Today_List)
                    print(f'Today is {Today} ')
                    break
                else:
                    print('Invalid date. Please check it again.')
        else:
            print('Use only digits')
    else:
        print('Please use "/" to separate date,month and year')

Feb=0
month_half = int(month/2)
if month>2:
    Feb=2
if month%2==0:
    Total_date= 31 * month_half +30 * (month_half-1)-Feb + date
else:
    Total_date = 31 * month_half + 30 * month_half - Feb + date

print(f'{Total_date} are over in {year}')

while True:
    ID=input('Enter your ID number: \n')
    Gender='His'
    if ID[:-1].isdigit():
        if ID[-1].lower()=='v':
            if len(ID)==10 or len(ID)==12:
                Total_date_Id = int(ID[-8:-5])
                year_Id= int(ID[:-8])

                if len(str(year_Id)) == 2:
                    year_Id=1900+year_Id
                if int(Total_date_Id)>500:
                    Gender = 'Her'
                    Total_date_Id = Total_date_Id - 500
                print(f'{Gender} birth is happened in {year_Id} and after {Total_date_Id} days')
                break
            else:
                print('Your ID number must have 9 or 11 digits)')
        else:
            print('You must have to enter "V" end of the ID number')
    else:
        print("Please only use digits")

if Total_date_Id <= Total_date:
    dif_year = year - year_Id
    dif_date = Total_date -Total_date_Id
else :
    dif_date= (365-Total_date_Id)+Total_date
    dif_year= year - year_Id -1
print(f'{Gender} age is {dif_year} year and {dif_date} days for {Today}')
