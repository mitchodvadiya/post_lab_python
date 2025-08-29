
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