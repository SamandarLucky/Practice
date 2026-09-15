''' CLASS
    (1) what is class
    (2) ordinary vs static properties
    (3) special methods

'''
print("===== What is class =====")
# class - blueprint for object creation!
# structure > state constructor method

class Person():
    #state
    message = "class state property"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #method
    def Introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed")

person1 = Person("Sam", 25)
person2 = Person("Martin", 35)
person_obj = Person("Jogn", 23)

# ordinary state property
print("person1_name:", person1.name)

# ordinary method
person1.Introduce()
person2.say_age()

print("===== Ordinary vs static properties =====")
new_message = Person.message
print("new_message:", new_message)

# Static method

Person.explain()
print("===== special/magic methods =====")
# Python's most common special methods are below:

class Car():
    # state
    description = "This class makes cars"
    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year
    # method
    def start_engine(self):
        print(f"the {self.name} start engine!")
    
    def stop_engine(self):
        print(f"the {self.name} stopped engine!")
    def __str__(self):
        return f"the car.name: {self.name} was produced in {self.year} year!"

my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("----")
your_car = Car("Toyota", 2026)
print(your_car)