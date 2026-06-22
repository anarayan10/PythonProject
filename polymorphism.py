"""def add(a,b,c=0):
    print(a+b+c)
add(2,3)
add(1,2,3)"""

"""class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")


a1 = animal()
a1.sound()"""

"""class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    pass
d1=dog()
d1.sound()"""

class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class birds(animal):
    def sound(self):
        print("bird makes sound")
d1=dog()
d1.sound()
# a function overrides an existing function is called polymorphism means a single function that can be changed based
#on the requirement . poly - many , morphy- changing accorindly(tamil-urumatram-chamelion)
b1=birds()
b1.sound()



