# lists are sequence of values where values can be of any type

cheeses = ["Cheddar", "Edam", "Gouda"]
primeNum = [2, 3, 5, 7, 11, "Thirteen"]

print(cheeses, primeNum)

# lists are mutable
primeNum[3] = "Seven"

print(primeNum)

# access last item of the list using -1
print(primeNum[-1])

# checking whether item is in list or not using in operator
print(3 in primeNum)
print("Seventeen" in primeNum)


# Traversing a list
for num in primeNum:
    print(num)

# using loops utilizing len and range
for i in range(len(primeNum)):
    print(primeNum[i])

# + to concatenate lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# * to repeat list
print([0, 1] * 4)

t = ["a", "b", "c", "d", "e", "f"]

print(t[3:])

# updating multiple values using slice operator
t[:3] = ["x", "y"]

print(t)
