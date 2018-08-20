f=open('dj.txt')
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print(f.readlines())

f.seek(0)
for l in open('dj.txt'):
    print(l)
newf=open('new.txt','w+')
newf.write("manoj is a good guy")
newf=open('new.txt')
print(newf.read())