
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

sorted_by_keys = dict(sorted(my_dict.items()))       # Sorts by keys
print(sorted_by_keys)
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))  # Sorts by values
