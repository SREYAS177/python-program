# Name        : Sreyas Suresh
# Roll Number : 55
# Class       : MCA

# Dictionary operations

student = {
    "name": "Sreyas",
    "age": 22,
    "course": "MCA"
}

print("Dictionary:", student)

# Sorting dictionary
print("Sorted dictionary:", dict(sorted(student.items())))

# Merging dictionaries
details = {
    "college": "ABC College",
    "mark": 85
}

student.update(details)
print("Merged dictionary:", student)

# Frequency counting
text = "apple banana apple orange banana apple"

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Frequency:", frequency)


# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Common or unique elements
common = set1 & set2
unique = set1 ^ set2

print("Common elements:", common)
print("Unique elements:", unique)