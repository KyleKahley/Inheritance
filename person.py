class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phonenumber = phone
        
    def print_person(name, address, phone):
        print(f'Name: {name}')
        print(f'Address: {address}')
        print(f'Phone Number: {phone}')
    

class Customer(Person): 
    def __init__(self, cn, ml):
        Person.__init__(self)
        self.__customernumber = cn 
        self.__mailing_list = ml

    def print_person(self, name, address, phone, cn, ml):
        print(f'Name: {name}')
        print(f'Address: {address}')
        print(f'Phone Number: {phone}')
        print(f' Customer Number: {cn}')
        if ml == "True":
            print(f'Mailing Status: True')
        else: 
            print('not on mailing list')




    

    

