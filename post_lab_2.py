
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