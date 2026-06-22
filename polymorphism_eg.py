"""class Vehicle():
    def start(self):
        self.started = True
        print("Vehicle started")
class Car(Vehicle):
    def start(self):
        self.started = True
        print("Car started")

v1 = Vehicle()
v1.start()

c1 = Car()
c1.start()"""

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department,name, salary):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)

m1 = Manager("CSE","Mario",45000)
m1.display()