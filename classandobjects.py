'''class goa:
    name = ""
    drink = ""
    def party(self):
        print("Let's party...")
    def beach(self):
        print("Enjoying the beach...")
ramesh = goa()
suresh = goa()
ramesh.name = "Ramesh"
suresh.name = "Suresh"

ramesh.drink = "yes"
suresh.drink = "no"
print(ramesh.name)
print("drink:", ramesh.drink)
print(suresh.name)
print("drink:", suresh.drink)
ramesh.party()
suresh.beach()'''

class laptop:
    price = 0
    processor = ""
    ram = ""
    def price(self):
        print("price:")
    def processor(self):
        print("processor:")
    def ram(self):
        print("ram:")
hp = laptop()
lenavo = laptop()
dell = laptop()
hp.price = 60000
lenavo.price = 40000
dell.price = 50000

hp.processor = " intel_7th_generation"
lenavo.processor = " intel_3rd_generation"
dell.processor = " intel_5th_generation"

hp.ram = "16gb"
lenavo.ram = "4gb"
dell.ram = "8gb"

print("hp.price:", hp.price, "hp.processor:", hp.processor, "hp.ram:", hp.ram, "hp.processor:", hp.processor)
print("lenavo.price:", lenavo.price, "lenavo.processor:", lenavo.processor, "lenavo.ram:", lenavo.ram)
print("dell.price:", dell.price, "dell.processor:", dell.processor, "dell.ram:", dell.ram)
