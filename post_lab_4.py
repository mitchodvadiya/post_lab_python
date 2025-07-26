### experiment no : 4
#code :

# Example of List in Python
ages = [19, 26, 29]
print(ages)
#Output: 

# Task
a = list(range(5))
print(a)
#Output:

b = list(range(5,10))
print(b)
#Output:

c = list(range(0,10,2))
print(c)
#output:

d = list(range(10,0,-2))
print(d)
#output:


List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)

# Inserts an element at the specified position.
List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2, 10087)
print(List)


List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
# Add List2 to List1
List1.extend(List2)
print(List1)

# 1. Python sum() Method
# Calculates the sum of all the elements of the List.
List = [1, 2, 3, 4, 5]
print(sum(List))
# output

# Task:
List = ['gfg', 'abc', 3]

numeric_sum = sum(x for x in List if isinstance(x, (int, float)))
print(numeric_sum)


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List = ['a','b','c','d','a']
print(List.count('a'))
# output:

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))
# output


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))
# output

# Task:
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2, 2))
# output

# 5. Python min() Method

# Calculates minimum of all the elements of List.
numbers = [5, 2, 8, 1, 9]
print(min(numbers))
# output

# 6. Python max() Method
# Calculates the maximum of all the elements of the List.
numbers = [5, 2, 8, 1, 9]
print(max(numbers))
# output

# 7. Python sort() Method
# Sort the given data structure (both tuple and list) in ascending order.
List = [2.3,4.445,3,5.33,1.054,2.5]
List.sort()
print(List)
# output


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse=True) 
print(List)   
# output


# 8. Python reverse() Method
# reverse() function reverses the order of list.
# creating a list
list = [1,2,3,4,5]
#reversing the list
list.reverse()
#printing the list
print(list)


# 1. Python pop() Method
# Removes an item from a specific index in a list.
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
# output

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(0))
# output

# 2. Python del() Method
# Deletes an element from the list using it’s index.
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)
# output


# Removes a specific element using it’s value/name.
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)
# output


# removing duplicates from a list using dictionaries
my_list_1 = [5, 2, 90, 24, 10, 2, 90, 34]
my_list_2 = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']

# removing duplicates from list 1
my_list_1 = list(dict.fromkeys(my_list_1))
print(my_list_1)

my_list_2 = list(dict.fromkeys(my_list_2))
print(my_list_2)

my_list_1 = [5, 2, 90, 24, 10]
my_list_2 = [6, 3, 91, 25, 12]

# combined
my_combined_list = list(zip(my_list_1, my_list_2))
print(my_combined_list)


my_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']
most_frequent_value = max(set(my_list), key=my_list.count)
print("The most common element is:", most_frequent_value)

list_of_lists = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]
# using list comprehension
my_list = [item for List in list_of_lists for item in List]
print(my_list)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#post lab : 4

# a. Multiply all the items in a list
from functools import reduce
list1 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list1)
print("Product of all items:", product)

# b. Get the largest number from a list
list2 = [10, 25, 3, 56, 7]
largest = max(list2)
print("Largest number:", largest)

# c. Remove duplicates from a list
list3 = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = list(dict.fromkeys(list3))
print("List after removing duplicates:", no_duplicates)

# d. Get the frequency of elements in a list
list4 = [1, 2, 2, 3, 3, 3, 4]
frequency = {x: list4.count(x) for x in set(list4)}
print("Frequency of elements:", frequency)

# e. Find common items from two lists
list5 = [1, 2, 3, 4]
list6 = [3, 4, 5, 6]
common_items = list(set(list5) & set(list6))
print("Common items:", common_items)

# f. Convert a list of multiple integers into a single integer
list7 = [1, 2, 3, 4]
single_integer = int(''.join(map(str, list7)))
print("Single integer:", single_integer)

