print("========= number ==========")
# Variable is a name of storage location (Java)
# Variable is a name of reference (chunki pythonda hamma narsa object)

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count() #method
result2 = count.numerator # state
print(result1, result2)

print("========= string ==========") 
#METHODS: upper() lower() title() find() replace()

# string lar primitive variable va state, method lariga ega ekan
course = "AI Python Fullstack"
result = type(course)
print(f"the result (1): {result}")
result = course.title() #bosh harflarini Katta qilib beradi
print(f"the result (2): {result}")

result = course.upper() #upper case boldi
print(f"the result (3): {result}")

result = course.replace("Fullstack", "MasterClass")
print(f"the result (4): {result}")

print("========= boolean ==========") 
# function > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY cs FALSY value
# TRUTHY > True  100 -100 "MIT"
# FALTHY > False : False 0 "" None

test_falsy = "" or False or None or 0 or 100
print("The falsy:", bool(test_falsy))

test_truthy = "MIT"
print("The truthy:", bool(test_truthy))