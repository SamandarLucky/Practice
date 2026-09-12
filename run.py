message = "Python: Everything is object!"
print(message)

result = type(message)
print("result:", result)

# Dunder double under score __builtins__ system - variable, __init__
# Name of reference - variable 

''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTIONS > print() len() input() type()
(3) CONSTANTS > True False None
'''

print(dir(__builtins__))