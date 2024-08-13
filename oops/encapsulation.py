
# make brand private and only accessible with a function
class Car():
    def __init__(self, brand, model):
        self._brand= brand
        self.model= model
    
    # getter function for brand access
    def get_brand(self):
        return self._brand +" !"
    
privateCar= Car("honda", "SUV")
print(privateCar.get_brand())
        


        