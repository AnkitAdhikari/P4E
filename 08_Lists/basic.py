# lists are sequence of values where values can be of any type

from os import remove


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

# list methods
list1 = [1, 2, 3, 4]

list1.append(5)
# now the list1 has 5 as list element

print(list1)

list2 = [6, 7, 8, 9, 10]

# method: extend (extend desired list with another list)

list1.extend(list2)

# list1 is now[1,2,3,4,5,6,7,8,9.10]
print(list1)

# method: sort (sort the intented list)
unsorted = [2, 34, 88, 23, 83, 74]
unsorted.sort()
print(unsorted)

# Dealiting elements
# method: pop takes index as argument and if left empty removes last element and return the removed element

removed = unsorted.pop(-1)

# if removed value is not required we can use del

example = ["a", "b", "c"]

del example[1]
print(removed)

# remove element using exact value

unsorted.remove(2)  # returns null

print(unsorted)

# remove multiple values using slicing
del unsorted[:-1]

print(unsorted)

# Lists and Functions
nums = [3, 41, 12, 9, 74, 15]

# These functions only works if the list elements are numbers
print(max(nums))
print(min(nums))
print(sum(nums))

# finding average utilizing functions
print(sum(nums) / len(nums))

# list and strings
s = "spam"
print(list(s))

s = "This is an example string"
fmts = s.split()

print(fmts)

# joining list elements
delimiter = " "
example_list = ["This", "string", "is", "supposed", "to", "be", "space", "formatted."]

fmt_output = delimiter.join(example_list)

print(fmt_output)

strA = "hello"
strB = "hello"

print(strA is strB)

lA = [1, 2, 3]
lB = [1, 2, 3]

# for list there is a unique object created for each list
print(lA is lB)


a = ["a", "b", "c"]


def delete_head(t):
    del t[0]


delete_head(a)

print(a)
