# example.py
def add(a, b):
    result = a + b
    return result


# importing the created module
import post_lab_8 as addition

a = addition.add(4, 5)
print("Addition using example module:", a)


# Import Python Standard Library Modules
import math
print("The value of pi is", math.pi)


# Python import with Renaming
import math as m
print("Pi using renamed module:", m.pi)


# Python from...import statement
from math import pi
print("Pi using from...import:", pi)


# Import all names
from math import *
print("Pi using import * :", pi)


# The dir() built-in function
import math
print("Functions in math module:", dir(math))


# List all built-in modules
help('modules')


# Find the area of a circle
r = 5
area = math.pi * r * r
print("Area of circle:", area)


# Print the values of positive and negative infinity
print("Positive infinity:", math.inf)
print("Negative infinity:", -math.inf)


# ----------------------------------------------------------------------------------------------------------------


# post_lab_8

import math

# 1. Convert degree to radian
def degree_to_radian(degree):
    return math.radians(degree)

deg = 180
print(f"{deg} degrees in radians is {degree_to_radian(deg)}")
# Output: 180 degrees in radians is 3.141592653589793


# 2. Simplest program for y = 6x^2 + 4sin(x)
def calculate_y(x):
    return 6 * x**2 + 4 * math.sin(x)

x = 2
print(f"y = {calculate_y(x)} when x = {x}")
# Output: y = 24.637189707302724 when x = 2


# 3. Function for f(x), f'(x), f''(x)
def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

x = math.pi
f, f_prime, f_double_prime = evaluate_functions(x)
print(f"For x = π : f(x) = {f}, f'(x) = {f_prime}, f''(x) = {f_double_prime}")


