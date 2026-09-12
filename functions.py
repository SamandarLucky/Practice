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


# DEFINE - build qismi
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeteing is executed")
    return f"Hi {b}"

# CALL - execute
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Samandar")
print("result2:", result2)