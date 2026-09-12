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