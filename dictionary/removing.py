
my_dict = {"name": "Alice", "age": 30, "city": "New York", "email":"az@gmail.com"}
age = my_dict.pop("age")  
# 31, removes 'age' from dictionary
print(age)
print(my_dict)
del my_dict["city"] 
print(my_dict)  
# Removes 'city' key-value pair
last_item = my_dict.popitem() # Removes and returns ('email', 'alice@example.com')
print(last_item)
my_dict.clear()               # Removes all items
