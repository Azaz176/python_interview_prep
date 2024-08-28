dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "email": "alice@example.com"}

dict1.update(dict2)# Merges dict2 into dict1
print(dict1)           
merged_dict = {**dict1, **dict2}  # Merges dict1 and dict2 into a new dictionary

print(merged_dict)