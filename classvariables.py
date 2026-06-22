class phone():
    chargertype = "c-type"
    def __init__(self, brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)

phone.chargertype = "b-type"

samsung = phone("samsung",10000)
samsung.display()

apple = phone("apple",70000)
apple.display()

"""this program teaches class variables like instance variables which changes dynamically with Values 
whereas class variable will not change.
class variables are defined below the class and not reqd to change it, incase of change 
we can define below the function and it will replicated everywhere in the program

Instance variables can be defined in a function as it keeps changing with the requirement"""