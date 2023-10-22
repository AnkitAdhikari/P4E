# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = int(input("Enter number of hours worked: "))
rate = int(input("Enter your rate: "))

if hours > 40:
    print("Your pay is: ", rate * 40 + (hours - 40) * rate * 1.5)
else:
    print("Your pay is: ", hours * rate)
