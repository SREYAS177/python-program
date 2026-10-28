# Accept comma-separated numbers

data = input("Enter numbers separated by comma: ")

# Generate list
numbers = [int(x) for x in data.split(",")]

# Generate tuple
numbers_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", numbers_tuple)

# Total number of elements
print("Total number of elements:", len(numbers))

# First element
print("First element:", numbers[0])

# Last element
print("Last element:", numbers[-1])

# Reverse list
print("List in reverse order:", numbers[::-1])