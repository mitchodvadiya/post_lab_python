code : 1
# Program to count lines, words, and characters in example.txt
with open("ict.txt", "r") as file:
    text = file.read()

# Count lines
line_count = text.count("\n") + 1 if text else 0  

# Count words
word_count = len(text.split())

# Count characters
char_count = len(text)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)


code : 2
# Program to read file line by line and store in a list
lines_list = []
with open("ict.txt", "r") as file:
    lines_list = file.readlines()   # keeps '\n'

# Remove '\n' from each line (optional)
lines_list = [line.strip() for line in lines_list]

print("List of lines:", lines_list)


code : 3

import csv

# Program to read and print rows of data.csv
with open("data-1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


code : 4

# Program to merge file1.txt and file2.txt into merged.txt
with open("ict.txt", "r") as f1, open("ict.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")   # optional, to separate files
    f3.write(data2)

print("Files merged successfully into merged.txt")


















