squares = [x**2 for x in range(6)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25]

fruits = ["apple", "banana", "cherry", "apple"]
another_copy = fruits[:]
print(another_copy)

for fruit in fruits:
    print(fruit)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])  # Output: 2
