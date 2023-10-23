# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program

try:
    hours = int(input("Enter the hours worked: "))
    rate = int(input("Enter rate per hour: "))
except:
    print("Error, please enter numeric input")

if hours > 40:
    print("Your pay is ", (hours - 40) * 1.5 * rate + hours * rate)
else:
    print("Your pay is: ", hours * rate)
