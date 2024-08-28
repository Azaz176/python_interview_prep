dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4} (merges dicts, with dict2 overwriting dict1)
