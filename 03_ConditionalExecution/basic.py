# Boolean expression (gives True or False)


print(5 == 5)  # True
print(5 == 6)  # False

result = 5 == 6
print(
    "True or False in python are evaluted as boolen/bool not as string", type(result)
)  # Data type


# '==' was one of the comparision operator
# other comparison opertor are given below

X = 20
Y = 10

# X is not equal to Y
print("20 is not equal to 10:", X != Y)  # True 20 is not equal to 10

# X is greater than Y
print("20 is greater than 10:", X > Y)  # True 20 is greater than 10

# X is less than Y
print("20 is less than 10:", X < Y)  # False 20 is not less than 10

# X is greater or equal to Y
print("20 is greter or equal than 10:", X > Y)  # True 20 is greter or equal than 10

# X is less than or equal to Y
print("20 is less or equal to 10:", X >= Y)  # False 20 is not less or equal to 10

# X is same as Y
print("20 is same as '20':", 20 is "20")  # False 20 is not same as "20"

# X is not the same as Y
print("20 is is not same as 20: ", 20 is not 20)  # False 20 is same as 20

# Logical Operators [and, or , not]

print("X > 0 and X < 10: ", X > 0 and X < 10)  # X(20) is between 0 and 10 -> False

n = 9
print(
    "9 is completely divisible by 2 or 3: ", n % 2 == 0 or n % 3 == 0
)  # True 2nd expression statisfies that 9 is completely divisible by 3

print("Opposite of 20 > 10 is", not (20 > 10))  # False not negets the result
