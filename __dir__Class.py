class MyClass:
    def __init__(self):
        self.attribute1 = 'value1'
        self.attribute2 = 'value2'

    def method1(self):
        pass

    def method2(self):
        pass

    def __dir__(self):
        # Return a custom list of attributes and methods
        return ['attribute1', 'attribute2', 'method1', 'method2', 'custom_method']

    def custom_method(self):
        pass

# Create an instance of the class
obj = MyClass()

# Use dir() to get the list of attributes and methods
print(dir(obj))
