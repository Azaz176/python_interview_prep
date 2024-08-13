# class MyClass:
#     class_var = 0  # Class variable

#     def __init__(self, instance_var):
#         self.instance_var = instance_var  # Instance variable
#         MyClass.class_var += 1  # Increment class variable

# # Creating instances
# obj1 = MyClass(1)
# print(obj1.class_var)  # Output: 1 (after increment)

# obj2 = MyClass(2)
# print(obj2.class_var)  # Output: 2 (after increment)

# MyClass.class_var = 10  # Changing the class variable

# obj3 = MyClass(4)
# print(obj3.class_var)  # Output: 11 (after increment)

# obj4 = MyClass(5)
# print(obj4.class_var)  # Output: 12 (after increment)

# print(MyClass.class_var)

class Car:
    totalCar=0
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        Car.totalCar+=1 #two cars are usingn this class

Car("Tesla", "modern")
Car("Honda", "i20")
print(Car.totalCar)