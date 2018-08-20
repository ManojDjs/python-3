class car:
    wheels=4
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def setvalues(self):
        self.color=str(input("enter color of car"))
        self.price=int(input("enter price of car"))
    def getvalues(self):
        print("color of car is %s" %self.color)
        print("price is %d" %self.price)
class bmw(car):
    def __init__(self,fuel):
        super(car).__init__()
        self.fuel=fuel
x=bmw(input(str())) 
x.setvalues()
x.getvalues()
print("wheels are %d" %x.wheels)
print("fuel is %s" %x.fuel)

