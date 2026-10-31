# List operations

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Create / add
numbers.append(60)
print("After adding:", numbers)

# Search
x = int(input("Enter number to search: "))

if x in numbers:
    print("Number found")
else:
    print("Number not found")

# Update
numbers[0] = 100
print("After updating:", numbers)

# Filter even numbers
even = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even)

# Sort
numbers.sort()
print("Sorted list:", numbers)

# Reverse
numbers.reverse()
print("Reversed list:", numbers)