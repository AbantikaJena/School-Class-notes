# List comprehention Chapter Que2

def unique(lst):
    L2=[]
    x = [L2.append(i) for i in lst if i not in L2]
    return(L2)
L = eval(input("Enter an array lst : "))
print(unique(L))
