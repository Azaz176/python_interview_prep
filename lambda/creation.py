#    lambda arguments: expression

# arguments: The input parameters to the lambda function.
# expression: The single expression that is evaluated and returned
# A lambda function that adds 10 to the input
add_ten = lambda x: x + 10

print(add_ten(5))  # Output: 15
# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y

print(multiply(2, 3))  # Output: 6

# Use lambda to square all elements in a list
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)

print(list(squared))  # Output: [1, 4, 9, 16]

# Use lambda to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # Output: [2, 4, 6]

# Use lambda as a key for sorting a list of tuples by the second element
pairs = [(1, 2), (3, 1), (5, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(3, 1), (1, 2), (5, 4)]
