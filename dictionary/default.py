my_dict = {"name": "Alice", "age": 30, "city": "New York"}

age = my_dict.setdefault("age", 40)  # Returns 31 if 'age' exists, otherwise adds 'age': 40


###The setdefault() method returns the value of a key if it exists. If the key does not exist, it inserts the key with the specified value.