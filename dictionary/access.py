my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name = my_dict["name"]       # 'Alice'
age = my_dict.get("age")     # 30
country = my_dict.get("country", "USA")  # 'USA' (default value if key not found)
print(name, age, country)