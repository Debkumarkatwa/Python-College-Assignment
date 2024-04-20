# String functions demonstration

# Length of a string
string = "Hello, World!"
length = len(string)
print("Length of the string:", length)

# Convert string to uppercase
uppercase_string = string.upper()
print("Uppercase string:", uppercase_string)

# Convert string to lowercase
lowercase_string = string.lower()
print("Lowercase string:", lowercase_string)

# Count occurrences of a substring
substring = "o"
count = string.count(substring)
print("Number of occurrences of 'o':", count)

# Check if a string starts with a specific substring
starts_with = "Hello"
if string.startswith(starts_with):
    print("String starts with '", starts_with, "'")

# Check if a string ends with a specific substring
ends_with = "World!"
if string.endswith(ends_with):
    print("String ends with '", ends_with, "'")

# Find the index of a substring
substring = "World"
index = string.find(substring)
print("Index of '", substring, "':", index)

# Replace a substring with another substring
old_substring = "World"
new_substring = "Universe"
new_string = string.replace(old_substring, new_substring)
print("New string:", new_string)

# Split a string into a list of substrings
split_string = string.split(",")
print("Split string:", split_string)