def squ(l):
    return l**2
# used to get along each iterable values to function
num=[2,4,5,6,7]
for i in map(squ,num):
    print(i)

l=list(map(lambda x:x**2,num))
print(l)
var=['manoj','sus','hon','ass']
s=list(map(lambda x:x[0],var))
print(s)
