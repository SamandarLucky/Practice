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