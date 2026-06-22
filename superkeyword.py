"""class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")

class b():
    def __init__(self):
        print("b")
    def display(self):
        print("you are in class b")

obj1 =b()
======"""
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")

class b(a):
    def __init__(self):
        super().__init__()
        #when super keyword is used it calls the parent class irrespective of the constructor defined in class a() and also after
        # print b along with parent class
        print("b")
    def display(self):
        print("you are in class b")

class c(b):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("you are in class c")

#obj1 =b()
obj1 = c()
# now after defining object B using class a constructor it fetches value from class b reason is that when there
#is not specific constructor defined for b it uses class a constructor and when it is defined it uses class b constructor
"""Key takeaway

class a:
    def __init__(self):
        print("A")

class b:
    def __init__(self):
        print("B")

class c(a, b): == will not work will throw MRO error 
    def __init__(self):
        super().__init__()
        print("C") 

Your code is mixing:

Single inheritance (b(a))
Multiple inheritance (c(a,b))

in a way that creates an MRO conflict.

For your current learning goal with super(), use:

class c(b):

and everything will work correctly."""

