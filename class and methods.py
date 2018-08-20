class manoj:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch =branch
    def getage(self):
        print(self.age)
    def setage(self,age):
        self.age=age

m = manoj('sk',90,'dental')
print(m.branch)
m.name="manoj"
m.age=21
m.branch='cse'
print(m.age)
m.getage()
m.setage(12)
m.getage()
o=manoj('manoj',25,'cse')
o.getage()
k=manoj('murthy',1000,'ece')
print(k.age)

