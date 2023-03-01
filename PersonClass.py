class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phonenumber = phone

    def get_name(self):
        return self.__name 
    def get_address(self):
        return self.__address
    def get_phonenumber(self):
        return self.__phonenumber  
    
        
    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address )
        print('Phone Number:', self.__phonenumber)
    

class Customer(Person): 
    def __init__(self, name, address, phone, cn, ml):
        Person.__init__(self, name, address, phone)
        self.__customernumber = cn 
        self.__mailing_list = ml

    def print_person(self):
        Person.print_person(self)
        print('Name:', self.__name)
        print('Address:', self.__address )
        print('Phone Number:', self.__phonenumber)

        print(f'Customer Number: {self.__customernumber}')
        if self.__mailing_list:
            print(f'Mailing Status: True')
        else: 
            print('not on mailing list')




    

    

