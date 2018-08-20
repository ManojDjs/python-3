import functools
l=[4,5,2,7,8,100]
a=functools.reduce(lambda x,y: x*y,l)
print(a)
even=[]
even_num=list(filter(lambda x: (x%2==0),l))
print(even_num)
k=list(map(lambda x,y:x+y,l,even))
print(k)
