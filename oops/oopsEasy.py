# class Student:
#     __numberOfStudent = 0  # private and class property-static
#     __nameOfSchool = "HPS"
    
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.__marks = marks  # private
#         Student.__numberOfStudent += 1  # increment class variable
    
#     def getMarks(self):
#         return self.__marks
    
#     def setMarks(self, newMarks, passcode):
#         if passcode == self.__auth():  # call the private method correctly
#             self.__marks = newMarks
#         else:
#             print("Invalid passcode!")
    
#     def __auth(self):  # correct method signature
#         return "101"  # private method
    
#     @staticmethod
#     def getSchoolName(): 
#         return Student.__nameOfSchool
#     @staticmethod
#     def setSchoolName(newSchoolName):
#         Student.__nameOfSchool=newSchoolName
#         return Student.__nameOfSchool
        

#     def study(self):
#         print("I am studying")
    
#     def play(self):
#         print("I am playing")

# # Creating instances
# s1 = Student("Goku", 3, 85)
# s2 = Student("Gohan", 6, 45)

# # Setting new marks for s1
# s1.setMarks(65, "101")
# print(s1.getMarks())  # Should print 65

# # Accessing the school name using the class
# print(Student.getSchoolName())  # Should print "HPS"

# # Accessing the school name using the instance (not recommended but possible)
# print(s1.getSchoolName())  # Should print "HPS"
# print(Student.setSchoolName("mait"))


# ## ENCAPSULATION
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance  # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}, New Balance: {self.__balance}")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: {amount}, New Balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount!")

#     def get_balance(self):  # public method to access private attribute
#         return self.__balance

# # Using the BankAccount class
# account = BankAccount("Alice", 1000)
# account.deposit(500)
# account.withdraw(200)

# # Trying to access the private balance attribute directly
# # print(account.__balance)  # This will raise an AttributeError

# # Using the public method to access the balance
# print(account.get_balance())  # Outputs the current balance


##############################INHERITANCE#####################

# class User:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def _login(self):
#         print("login")

#     def logout(self):
#         print("logout")

# class Student(User):
#     pass

# # Create an instance of Student with required arguments
# s1 = Student("Alice", 101)

# # Call the login method
# s1._login()

class Parent:
    parentName = "XYZ"
    
    def __init__(self, totalChildren, income, totalHouse):
        self.totalChildren = totalChildren
        self.income = income
        self.totalHouse = totalHouse
        
    def __printIncome(self):
        print(f"total income is {self.income}")
        
    def _protectedHouse(self):
        print(f"total house {self.totalHouse}")
        
    def printChildren(self):
        print(f"total children {self.totalChildren}")

class Child(Parent):
    def __init__(self, parentName, childName, siblings, totalChildren, income, totalHouse):
        super().__init__(totalChildren, income, totalHouse)  # Call the Parent's __init__ method
        self.parentName = parentName
        self.childName = childName
        self.siblings = siblings
        super().printChildren()
        # super().income## cannot access attribute with super, only methods
    
    def callParentMethod(self):
        print("calling parent method")
        super().printChildren()

c1 = Child("Saif", "Taimur", 3, 2, 50000, 1)  # Pass the necessary arguments for Parent
print(c1.totalChildren)
c1.callParentMethod()


################### POLYMORPHISM ############################3
# ## 1. Method Overloading
# class Deatils:
#     def __init__(self, name, phone, address=""):
#         if(address==""):
#             self.two(name, phone)
#         else:
#             self.one(name, phone, address)
            
#     def one(self, name, phone, address):
#         self.name=name
#         self.phone=phone
#         self.address= address
        
#     def two(self, name, phone):
#         self.name=name
#         self.phone=phone
        
# c1= Deatils("az", 87, "delhi")
# print(c1)


## 2. Method Overriding
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Bark!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# def animal_sound(animal):
#     animal.speak()

# # Create instances of Dog and Cat
# dog = Dog()
# cat = Cat()
# animal= Animal()
# # Use polymorphism to call the speak method
# animal_sound(dog)  # Output: Bark!
# animal_sound(cat)  # Output: Meow!
# animal_sound(animal)


############## ABSTRACTIN ######################