fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ["apple", "blueberry", "cherry", "orange"]
fruits.insert(1, "kiwi")
print(fruits)  # Output: ["apple", "kiwi", "blueberry", "cherry", "orange"]
fruits.extend(["mango", "grapes"])
print(fruits)  # Output: ["apple", "kiwi", "blueberry", "cherry", "orange", "mango", "grapes"]
