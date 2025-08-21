# # Example 1
x = 10
if x > 5:
    print("x is greter than 5")

# # Example 2
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# # Example 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Nested if-else Example 1
age = 35
if age >= 60:
    print("You are a senior citizen.")
else:
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a teenager.")

# Nested if-else Example 2
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive but odd.")
else:
    print("The number is not positive.")

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Break statement
for x in range(1, 6):
    if x == 3:
        break
    print(x)

# Continue statement
for x in range(1, 6):
    if x == 3:
        continue
    print(x)

# Pass statement
for x in range(1, 6):
    if x == 3:
        pass
    print(x)

# Try-Except Example
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Built-in Function Example
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# User-defined Function Example
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)

# Lambda Function Example
add = lambda x, y: x + y
print(add(3, 5))

# Recursive Function Example
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Higher-Order Function Example
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Generator Function Example
def generate_numbers():
    for i in range(1, 6):
        yield i
for number in generate_numbers():
    print(number)


# -----------------------------------------------------------------------------------------------------------------
# post lab exercise :# 6

# a
num = 1
while num <= 100:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1

# b
# Program to find sum of all natural numbers from 1 to n

n = int(input("Enter a number: "))
total = n * (n + 1) // 2   
print("Sum of natural numbers from 1 to", n, "is:", total)

# c
# Function to count digits in a number

def count_digits(num):
    return len(str(abs(num)))  

# Exam
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

# d
# Program to find first and last digit of a number

num = int(input("Enter a number: "))
num_str = str(abs(num))

first_digit = int(num_str[0])
last_digit = int(num_str[-1])

print("First digit:", first_digit)
print("Last digit:", last_digit)

# # e
# Program to swap first and last digits

num = int(input("Enter a number: "))
num_str = str(abs(num))

if len(num_str) == 1:
    swapped = num_str
else:
    swapped = num_str[-1] + num_str[1:-1] + num_str

if num < 0:
    swapped = '-' + swapped

print("Number after swapping first and last digits:", swapped)

# f
# Program to calculate product of digits

num = int(input("Enter a number: "))
num_str = str(abs(num))

product = 1
for digit in num_str:
    product *= int(digit)

print("Product of digits:", product)

# g
# Program to reverse a number

num = int(input("Enter a number: "))
reverse_num = int(str(abs(num))[::-1])

if num < 0:
    reverse_num = -reverse_num

print("Reversed number:", reverse_num)
