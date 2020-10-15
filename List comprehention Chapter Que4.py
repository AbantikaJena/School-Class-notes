# List comprehention Chapter Que4

def Find_comman(L1,L2):
    L3=[]
    x = [L3.append(i) for i in L1 if (i in L1) and (i in L2) and (i not in L3) ]
    print(L3)
L1 = eval(input("Enter an list 1 : "))
L2 = eval(input("Enter an list 2 : "))
Find_comman(L1,L2)
