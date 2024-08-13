class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        
    def fuel_type(self):
        return "petrol and diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def fuel_type(self):
        return "Electric Charge"
    
safari= Car("Tata", "Safari")
print(safari.fuel_type())
testla= ElectricCar("Tesla", "Model S")
print(testla.fuel_type())