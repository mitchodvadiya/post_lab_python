# experiment no : 1
# code : 1

s = "welcome to python"
for i in range(5):
    print(s[0:17])


# code : 2

print("Number\tSquare\tCube")
for i in range(1, 5):  
    print(f"{i}\t{i**2}\t{i**3}")


# code : 3

numerator = 9.5 * 4.5 - 2.5 * 3
denominator = 45.5 - 3.5

result = numerator / denominator

print("Result is:", result)

########################################################################################################

# experiment no : 2
# code : 1
#Write a python code for calculating the Area and Perimeter of a Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))


area = length * width
perimeter = 2 * (length + width)

# Output
print("Area =", area)
print("Perimeter =", perimeter)

# code : 2
#Write a python code for testing if a number is even or odd
a = int(input("Enter the number: "))

if(a % 2 == 0):
    print("Even")
else:
    print("Odd")

# code : 3
#Write a python code for calculate the area and volume of the Cube.
side = float(input("Enter the side length of the cube: "))

# Calculations
area = 6 * side * side       
volume = side * side * side  

# Output
print("Surface Area =", area)
print("Volume =", volume)


# code : 4
# Write a python code to solve the equation z = (x+y)*(x-y)
x = int(input("Enter the number: "))
y = int(input("Enter another number: "))

z = (x + y) * (x - y)
print(z)

# code : 5
#Write a python code to solve the equation z = (x+y)*(x+y)-2xy; write a comment on it. 


x = int(input("Enter the number: "))
y = int(input("Enter another number: "))

z = ((x + y) * (x + y) - 2 * x * y)
print(z)

# code : 6
#Write a python code for Converting Celsius to Fahrenhit
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32


print("Temperature in Fahrenheit:", fahrenheit)

########################################################################################################

#experiment no : 3
#code : 1
#Write a Python program to reverse a string.
text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)

# code : 2
#Write a Python program to check if a string is a palindrome.
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not a palindrome")

# code : 3
#Write a Python program to check if a string contains only digits.
s = input("Enter a string: ")

# Check if the string contains only digits using isdigit()
if s.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain digits.")

# code : 4
#Write a Python program to find the longest word in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))

# code : 5
#Write a Python program to find the length of the last word in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.strip().split()

if words:
    print("Length of last word:", len(words[-1]))
else:
    print("No words in the sentence.")
