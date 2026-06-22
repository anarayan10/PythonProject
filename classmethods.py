class laptop():
    chargertype = "C-TYPE"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)
    @classmethod
    def changeChargetype(cls):
        cls.chargertype="B-TYPE"
        print("the charger type is changed to B-TYPE")
    @staticmethod
    def info():
        print("This is laptop class")
hp=laptop()
hp.setPrice(30000)
hp.getPrice()

laptop.changeChargetype()
hp.info()

"""This program is about using class methods.Methods are also functions. the classmethod is used to refer the class variable
and instead of writing (cls) everywhere we are using the decorator called @classmethod and @staticmethod is also decorator 
A static method in Python is a method bound to a class rather than its objects, meaning it can be called without creating a class instance. It is defined using the @staticmethod decorator and does not accept any implicit first arguments like self or cls.Quick Examplepythonclass MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Call directly using the class name
result = MathUtils.add(5, 10)
print(result)  # Output: 15
Use code with caution.Core CharacteristicsNo State Access: It cannot modify or read instance state (self) or 
class state (cls).Namespace Isolation: It behaves like a normal function 
but lives inside a class namespace for better code organization.
Flexible Calling: You can invoke it using ClassName.method() or on an instantiated object like object.method()."""
