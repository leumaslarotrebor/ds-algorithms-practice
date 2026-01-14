# Linear search example

numbers = [5, 8, 12, 20, 35]
target = 20

found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
