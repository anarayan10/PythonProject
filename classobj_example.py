class teacher:
    def __init__(self,name,regnum):
        self.name = name
        self.regnum = regnum
    def display(self):
            print("name:", self.name)
            print("regnum:", self.regnum)

t1=teacher("deepak", 2222)
t2=teacher("deepa", 2223)

t1.display()
t2.display()