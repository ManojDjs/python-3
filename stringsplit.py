def st(name):
    str=''
    k=len(name)
    for l in range(0,k):
        if(l%2==0):
           str=str+name[l].upper()
        else:
            str=str+name[l].lower()
    print(str)
st('manoj')