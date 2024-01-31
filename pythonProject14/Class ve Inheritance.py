#%% property
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName =firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Emre","Uludag",20)
print(person1.firstName)

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary

class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()

mehmet = Customer()









