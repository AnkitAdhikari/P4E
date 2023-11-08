# A string is a sequence of characters. You can access the characters one at a time with the bracket operator

fruit = "banana"
print(fruit[0], fruit[2], fruit[-1])  # string index starts from 0


# getting length of the string using len()

print("The length of the fruit variable", len(fruit))


# string is iterable
# with for loop
print("Printing letters with for loop")
for letter in fruit:
    print(letter)

# with while loop
print("Printing letters with while loop")
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1

# slicing string
s = "Monty Python"
print("String to slice => ", s)
print("slicing first five letters of the string => ", s[0:5])
print("Slicing can also be done from middle => ", s[6:])

# note: String is immutable i.e it's must be re initialized if we want to change a even a value of the particular index


# looping in string
count = 0
for char in "hello":
    if char == "l":
        count += 1
print("The number of l in word hello is", count)


# the in operator with string

print("using in operator with string")

print("Does word banana has letter z:", "z" in "banana")

print("Does word zebra has letter z:", "z" in "zebra")

# String comparison

word = input("Input a word for string comparison: ")

if word == "banana":
    print("All right, bananas.")

# other operators can be used for putting words in order

if word < "banana":
    print("Your word," + word + ", comes before banana")
elif word > "banana":
    print("Your word," + word + ", comes after banana.")
else:
    print("All right, bananas")

# try to convert string to lowercase before comparing becuase this my help to solve the conflit between uppercase and lowercase problem while comparing

# string methods
# the upper method
new_word = word.upper()
print(new_word)

# the find method
index = word.find("a")  # second arg denote the start point of the method
print(index)

# the strip method (remove whitespace form the beginning and end of the string)
line = "   Here we go. "
print(line.strip())

# startswith method
line = "Have a nice day"
print(line.lower().startswith("h"))
