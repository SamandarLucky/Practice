''' FUNCTIONS
(1) DEFINE & CALL
(2) Parametr & Argemunt
(3) Keyword & Default arguments
(4) Scope
'''

print("===== DEFINE & CALL =====")
# build in function > print() type()
# Function - malum bir mantiqni ishga tushuruvchi code block
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - build qismi - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeteing is executed")
    return f"Hi {b}"

# CALL - execute - argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Samandar")
print("result2:", result2)

print("===== Keyword & Default arguments =====")
# DEFINE
def give_greet(name, age=22):
    print("give greet is executed")
    return f"Hi {name}, you are {age} years old!"

result3 = give_greet(name="Samandar", age=24)
print("result3:", result3) #source yanada aniqroq

result4 = give_greet("John")
print("result4:", result4) 