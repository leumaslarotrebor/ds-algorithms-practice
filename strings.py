# String practice problems

# Reverse a string
text = "python"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Check palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
