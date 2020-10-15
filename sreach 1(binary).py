
def linearsearch(thearray,search):
    ctr=0
    pos=0
    n=len(thearray)
    while (ctr<=n-1):
        if(thearray[ctr]==search):
            pos = ctr
            return True,pos
        else:
            ctr+=1
    return False,pos
L=[10,51,2,18,4,31,13,5,23,64,29]
p= linearsearch(L,31)
print(p)