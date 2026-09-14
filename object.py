''' OBJECT -malum bir maqsad bilan yaratilgan o'zini method va property ega bo'lgan datatype

'''
import array #package/module
import math
from math import ceil, asin

print("===== What is object =====")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction, Encapsulation, Polimorphism, Inheritence
result1 = math.ceil(97.7) # Call
print("result1:", result1)

result2 = ceil(98.8)
print("result2:", result2)

print("===== Error handling system =====")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
   print("passed here")
   result = car_dict["origin"]
   print("result", result)
except KeyError as err:
    print("No origin state property found", err)
else:
    print("Executed successfully")
finally:
    print("Final closing logic")

