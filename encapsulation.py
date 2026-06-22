class company():
    def __init__(self):
        self._companyName= "Google"
class b (company):
    pass
b1=b()
print(b1._companyName)

# In this module, giving company name in class can be is like restricted access to modify
#the variable name google and also it can be accessed within the class is called
#encapsulation and ._company name is called private
#and __access restricted from modifying and accessed publicly
