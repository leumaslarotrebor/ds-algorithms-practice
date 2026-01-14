# Array practice problems

# Find the largest element in an array
numbers = [10, 45, 2, 89, 34]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# Reverse an array
reversed_array = numbers[::-1]
print("Reversed array:", reversed_array)
