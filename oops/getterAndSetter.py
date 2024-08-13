class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer")

# Example usage
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.set_name("Bob")
person.set_age(35)
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 35

# The following will raise an exception
# person.set_age(-10)
# person.set_name(123)
