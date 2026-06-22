"""Inheritence is a way of calling parent class from sub class or another call which will inherit the values of parent class

example program for Understanding:"""

#In this program we created a class called dad() in which we defined dad has a phone
#created another class called son() in which we defined son has laptop
#but son needs to access the dad's phone , hence we are defining dad in the son class inside the braces
#hence it can be inherited the from parent class dad by subclass son. this is called inheritance

class dad():
    def phone(self):
        print("Dad's phone")
class mom():
    def sweet(self):
        print("Mom's sweet")
class son(dad,mom):
    def laptop(self):
        print("Son's laptop")
ram = son()
ram.phone()
ram.sweet()

# created another class called the mom class and now son class needs to access the mom class
#hence we defined the son class with "class son (mom,dad). hence output will print statement of dad and mom.--this is
#called multiple inheritance because it can access both the classes

#multilevel inheritance: grandpa class has phone, dad class has money and son class has laptop now son needs money so he uses dad class
#dad needs phone hence he uses grandpa class . Means each class is access another class and it is connected .
#now son class can access both dad and grandpa class as they are connected
#

class grandpa():
    def phone(self):
        print("Grandpa's phone")
class dad(grandpa):
    def money(self):
        print("Dad's money")
class son(dad):
    def laptop(self):
        print("Son's laptop")
ram=son()
ram.laptop()
ram.phone()
ram.money()
daddy=grandpa()
daddy.phone()

#hierarchial inheritance example:
#if dad class is used by other classes means only one class is there but used by all means it is called hierarchial class
class dad()
    def money(self):
        print("Dad's money")
class son1():
    pass
class son2():
    pass
class son3()
    pass

s1 = son2()
s2.money()

#hybrid inheritance: using all the classes together is called hybrid class(single, multiple,multilevel , hierachical )

class dad()
    def money(self):
        print("Dad's money")
class land():
    def important(self):
        print("Land's important")
class son1():
    pass
class son2():
    pass
class son3()
    pass

s1 = son2()
s2.money()
