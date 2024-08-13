class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __str__(self):
        if self.real == 0:
            return f"{self.img}j"
        elif self.img < 0:
            return f"{self.real}{self.img}j"
        else:
            return f"{self.real} + {self.img}j"

    def __add__(self, other):
        rN = self.real + other.real
        iN = self.img + other.img
        return ComplexNumber(rN, iN)
    
    def conjugate(self):
        return ComplexNumber(self.real, self.img*-1)
    
cn1 = ComplexNumber(3, -8)
cn2 = ComplexNumber(1, 2)

print(cn1 + cn2)
c3= ComplexNumber(5,-9)
print(c3.conjugate())
