#create a class called calculator
#create 2 variables a and b
#create a function called add, sub, mul and div should take 2 variables as parameters
#Pass the a and b value through object()


class calculator:
    def __init__(self,a,b):
        self.number1 = a
        self.number2 = b

    def add (self):
        self.addition = self.number1 + self.number2

    def sub(self):
        self.subtract = self.number1 - self.number2


    def mul(self):
        self.multiply = self.number1 * self.number2

    def div(self):
        self.div = self.number1 % self.number2


    def display(self):
        print("addition:", self.addition)
        print("subtract:", self.subtract)
        print("multiply:", self.multiply)
        print("division:", self.div)

obj = calculator(90,5)

obj.add()
obj.sub()
obj.mul()
obj.div()

obj.display()