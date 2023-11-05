# 1) updating variable
x = 0
# a variable must be defined before it is updated
x = x + 1  # updating / incrementing the value of x by one

# using while statements

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# usuage of infininte loop
while True:
    line = input(">")
    if line == "done":
        break  # break keyword is used to terminate loop
    print(line)
print("Done!")


# usuage of continue keyword for skipping to next iteration

while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")


# Another loop statement => for statement
# good for looping set of things

friends = ["Julian", "Bob", "Jasmine", "Aurther"]

for friend in friends:
    print("Happy New Year:", friend)
print("Loop completed")


# finding sum of the number in the list
total = 0
for num in [1, 2, 3, 4, 5]:
    total = total + num
print("The sum of the list is", total)


# finding the largest value in a list

largest = None  # None is a keyword in python when can be assigned to a variable to denote that the assigned variable is empty

for num in [2, 52, 11, 83, 11, 23]:
    if largest is None or num > largest:
        largest = num
print("The largest number is", largest)


# finding the smallest value in a list

smallest = None
for num in [2, 52, 11, 83, 11, 23]:
    if smallest is None or num < smallest:
        smallest = num
print("The smallest number is", smallest)
