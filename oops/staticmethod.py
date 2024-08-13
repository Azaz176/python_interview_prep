#static method->In Python, static methods are a type of method that belongs to the class rather than any instance of the class. This means that they can be called on both the class itself and any of its instances. The reason for this flexibility is Python’s dynamic nature and its underlying method resolution order (MRO).When you call a method on an instance, Python first checks if the method is defined in the instance itself. If not, it then checks the class of the instance and proceeds up the inheritance hierarchy. Since static methods are defined at the class level, they are accessible from both the class and the instance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @staticmethod
    def general_description():
        return "Cars are amazing"
    
# Accessing the static method through the class
print(Car.general_description())

mycar= Car("tesla", "bb")
print(mycar.general_description())# both can access 