my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:
    print(key, my_dict[key])  # Iterates over keys

for value in my_dict.values():
    print("key->",value)
for key, value in my_dict.items():
    print(key, value)         # Iterates over key-value pairs
