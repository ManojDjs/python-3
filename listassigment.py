str="Santosh is a playful young NRI from London, who returns to India to attend his cousin Lali wedding.There, he meets one of Lalita's friends, Siri who came from the countryside to attend the marriage.Though they initially clash,after a series of misadventures,they fall in"
listl=[]
for f in str.split():
    if len(f)%2==0:
        listl.append(f)
print(listl)
k=[x for x in str.split() if len(x)%2==0]
print(k)
k=[x for x in range(0,100)]

