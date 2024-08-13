class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
        
    def carfullname(self):
        return f"{self.brand} {self.model}"
        
# firstcar= Car("toyota", "safari")
# print(firstcar.brand, firstcar.model)
# secondcar= Car("suzuki", "i20")
# print(secondcar.model, secondcar.brand)
# print(secondcar.carfullname())

## INHERITANCE- ELECTRIC CAR WITH BATTERY SIZE

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)#inheriting brand and model
        self.batterSize= batterySize
        
teslacar= ElectricCar("Tesla", "model s", "85kwh")
print(teslacar.model)
print(teslacar.batterSize)
print(teslacar.carfullname())
