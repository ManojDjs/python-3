dict={'k1':'manoj','k2': 4.7 ,'k3':999}
print(dict['k1'][::-1])
print(dict['k2'] + 3)
print(dict)
dict['k2']=dict['k2']+100
print(dict)
dict['k3']+=1000
print(dict)
l={}
print(l)
l['manoj']='good guy'
l['sk']='topper'
print(l.keys())
k=int(input("enter values you want to enter"))
for i in range(k):
    v=str(input())
    l['ll']=v
print(l.values())
list=[1,5,8,9]
l['num']=list
print(l)