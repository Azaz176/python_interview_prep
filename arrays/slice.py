fruits = ["apple", "banana", "cherry", "apple"]
sub_list = fruits[1:3]
print(sub_list)  # Output: ["banana", "cherry"]

# Omitting the start or end index
print(fruits[:2])  # Output: ["apple", "banana"]
print(fruits[2:])  # Output: ["cherry", "apple"]

# Using step in slicing
print(fruits[::2])  # Output: ["apple", "cherry"]
