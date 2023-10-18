# assigining different type of value to variables
message = "And now for something completely different"  # a string is being assigned
n = 17  # a ineger is being assigned
pi = 3.1415926  # a floating number is being assigned ( decimal number)

print(message)  # printing variable's value to the console

print(type(message))  # printing the data type of the varible using type() function

# operators
print("Add 20 + 32 = ", 20 + 32)  # additon

print("Sub 30 - 10 = ", 30 - 10)  # subtraction

print("Multiply 2 * 3 = ", 2 * 3)  # multiplication

print("Divide 10 / 5 = ", 10 / 5)  # division (floating pont number is defalut)

print("2 to it's 4th power = ", 2**4)  # exponents

print("For integer output division, 10 // 5 =", 10 // 5)

# The reminder operator
print("The reminder of 7 / 5 is ", 7 % 5)

# Input function for taking user input
inp = input("What is your name?\n")
print(inp)  # prints what the user inputted

# use of int() function to convert sting-number to number

num = int("24")
print(num, "\n", type(num))
