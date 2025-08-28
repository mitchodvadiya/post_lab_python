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

