class hotel:
    my_dict={'Menu':('rice','chicken','dhal'),'table':tuple(x for x in range(6))}
    def __init__(self):

        self.custom_Order= {'meal': [], 'table': 0}
    def addMenu(*food):
        my_dict['Menu']+=food
        print(my_dict['Menu'],my_dict['table'])

    def printMenu(self):
        print(my_dict['Menu'])
    def get_mealOrder():

        while(True):
            meal=input('What do u want:\n')
            if meal in my_dict['Menu']:
                custom_Order['meal'].append(meal)
            else:
                print('sorry .that meal is not available')
            ans=input('do u want another one(y/n): ')
            if ans.lower()=='n':
                break
    def printTable(self,*value):
        print(my_dict['Book table'])
    def get_tableOrder(self):
         table=input("Enter your table number:")
         custom_Order['table']=table
    def print_customOrder(self):
        print('your Order list is: ',custom_Order['meal'])
        print('your table is: ',custom_Order['table'])
my_dict={'Menu' : ['rice','chicken','dhal'], 'Book table':[2,5,7,8]}

custom1 = hotel()
hotel.addMenu('chicken','egg','dhal','rice')
custom1.printMenu()
custom1.get_mealOrder()
custom1.printTable(2,3,4)
custom1.get_tableOrder()
custom1.print_customOrder()
