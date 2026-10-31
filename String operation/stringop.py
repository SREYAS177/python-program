# Name        : Sreyas Suresh
# Roll Number : 55
# Class       : MCA
# String processing operations

text = input("Enter a string: ")

# Character replacement
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")

print("After character replacement:", text.replace(old_char, new_char))

# String reversal
print("Reversed string:", text[::-1])

# Palindrome checking
if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Character frequency
char = input("Enter a character to find its frequency: ")
print("Frequency of", char, ":", text.count(char))

# Word frequency
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")

for word, count in frequency.items():
    print(word, ":", count)