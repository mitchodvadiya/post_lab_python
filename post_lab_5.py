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

