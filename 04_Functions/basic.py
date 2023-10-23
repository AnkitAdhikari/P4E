# Built-in functions

# max()
print(max("Hello world!"))  # largest value is w

# min()
print(min("Hello world!"))  # smallest value is ' '(space)

# len()
print(len("FOUR"))  # length of the strign 'FOUR' -> 4

# NOTE: we should treat names of built-in functions as reserved words and avoid uisng them as variable name (eg:max)

# type conversion functions

# int()
print("Converts 4.23 to 4 -> ", int(4.23))

# float()
print("Converts 4 to 4.0 -> ", float(4))

# str()
print("Converts a number such as 4 to '4' -> ", str(4), type(str(4)))


# Math functions

# importing math module

import math

print(math.pi)  # getting value of PI using math module

print(math.sqrt(64))  # sqrt from math module

# Random numvers

# importing random module

import random

for i in range(10):
    print(random.random())


# to get random iteger value btwn interval

print(random.randint(1, 10))


# choose value randomly
print(random.choice([1, 2, 3, 4]))

# Adding new functions

# Defining a functin called print_lyrics


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and work all day.")


# calling functions
print_lyrics()

# reusing created function inside other function


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


# calling repeat_lyrics()
repeat_lyrics()

# Parameters and arguments


def print_twice(me):
    print(me)
    print(me)


print_twice("Hello")


# Fruitful function ( a function returning sth)


def sum(a, b):
    return a + b


x = sum(1, 2)
print(x)
