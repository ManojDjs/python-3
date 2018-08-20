class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print('owner:{} and availabe balance is:{}'.format(self.owner,self.balance))
    def credit(self):
        x=int(input("amount you wanna credit:\n"))
        self.balance=(self.balance)+x
        print("your available balance is {}".format(self.balance))
    def debit(self):
        x = int(input("amount you wanna withdraw:\n"))
        if(self.balance<x):
            print("Insuffecinet funds,use less amount!")
        else:
            self.balance=self.balance-x
            print("available balance is{}".format(self.balance))
r= BankAccount(input("Enter the onwer name with which accout have to create:\n"), 0)
print("your banka account created with above credentials :\n")
while(True):
    print("enter operations you wanna do, \n1.credit. \n2.debit \n3.quit")
    choice=int(input("enter your choice:\n"))
    if(choice==1):
        r.credit()
    elif(choice==2):
        r.debit()
    else:
        quit()
