import PersonClass as p


name = 'Kyle'
address = '1234 Main st'
phone = '123-456-7890'
cn = 1229
ml = True

person1 = p.Person(name, address, phone)
customer1 = p.Customer(name, address, phone, cn, ml)

person1.print_person()

