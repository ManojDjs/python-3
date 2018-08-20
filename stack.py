class stack:
        stack=[]
        def add(self):
            x.value=input("enter the value that you wanted to add:")
            x.stack.append(x.value)
            print("value added successfully")
        def remove(self):x.stack.pop()
x=stack()
while(1):
    print("stack operations:")
    print("1.push\n2.pop\n3.show\n4.exit")
    choice=int(input("enter your choice:\n"))
    if choice==1:x.add()
    elif choice==2:x.remove()
    elif choice==3:
        l=len(x.stack)
        for i in range(l):
            print(x.stack[l-i-1])
    elif choice==4:break