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

