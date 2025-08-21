# Create a Python Tuple
numbers = (1, 2, -5)
print(numbers)


a_tuple = (0, [1, 2, 3], (4, 5, 6), 7.0)
print(a_tuple)

# # Access Tuple Items
languages = ('Python', 'Swift', 'C++')
print(languages[0])

# # Python Tuple Length
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars))

# Task
a = tuple(range(5))
print(a)

b = tuple(range(5, 10))
print(b)

c = tuple(range(0, 10, 2))
print(c)

d = tuple(range(10, 0, -2))
print(d)

# Extract 6 from nested tuple
d = (3, [5, 6, 7], (4, 5, 6), [5, 6, 7, (6, 7, 8)], 9, 10)
print(d[1][1])
print(d[2][2])
print(d[3][3][0])

# Important Functions
t1 = (2, 3, 4, 5)
print(sum(t1))

t3 = (3, 4, 4, 2, 2, 3, 6, 7, 4, 4)
print(t3.count(4))

# index() Method
print(t3.index(2))
print(t3.index(4, 3, 9))

# min() Method
print(min(t3))

# max() Method
numbers = (7, 2, 8, 5, 9)
print(max(numbers))

# Removing duplicates
a = (5, 6, 7, 5, 5, 9, 7)
b = ("a", "b", "v", "b")
my_tu_1 = tuple(dict.fromkeys(a))
print(my_tu_1)
my_tu_2 = tuple(dict.fromkeys(b))
print(my_tu_2)

# Combining tuples
first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = tuple(zip(first_names, last_names, ages))
print(zipped)

# Flatten a tuple of tuples
b = ((1, 2), (3, 4), (5, 6))
my = tuple(item for l in b for item in l)
print(my)


# -------------------------------------------------------------------------------------------------------------------

# post -lab exercise :# 5

# a. Count the occurrences of an element in a tuple
t = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))

# b. Check if an element exists in a tuple
t = (10, 20, 30, 40, 50)
print(30 in t)
print(100 in t)

# c. Convert a tuple to a string
t = ('P', 'y', 't', 'h', 'o', 'n')
s = ''.join(t)
print(s)

# d. Find the maximum and minimum elements in a tuple
t = (12, 5, 89, 34, 22)
print("Max:", max(t))
print("Min:", min(t))

# e. Convert a tuple of strings to a single string
t = ("Hello", "World", "Python")
s = " ".join(t)
print(s)

# f. Sort a tuple of integers
t = (9, 1, 8, 3, 7, 2)
sorted_t = tuple(sorted(t))
print(sorted_t)

# g. Find the first and last elements of a tuple
t = (11, 22, 33, 44, 55)
print("First:", t[0])
print("Last:", t[-1])
