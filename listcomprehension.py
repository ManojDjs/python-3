l=[]
for letter in "manoj":
    l.append(letter)
print(l)
m=[w  for w in "sorry"]
print(m)
sq=[r**2 for r in range(10)]
print(sq)
ev=[n for n in range(100) if(n%2==0)]
print(ev)
""" evry no to power of 4 with double list comprehension"""
fp=[i**2 for i in [j**2 for j in range(5) ] ]
print(fp)
string='manoj is good guy'
a=0
b=0
lis=[]
string=string+" "
for count in string:
    if(count==" "):
        l=string[a:b]
        a=b+1;
        lis.append(l)
    b=b+1;
print(lis)

s=[word[0] for word in lis]
print(s)
swt=[w for w in lis if(w[0]=='g')]
print(swt)