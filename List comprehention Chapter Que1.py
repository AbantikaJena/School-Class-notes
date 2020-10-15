# List comprehention Chapter Que1

def find_in_list(L, v ):
    for i in range(len(L)):
        if v==L[i]:
            break
        else:
            i=-1
    print("The 1st occurance of ",v," index number : ",i)
L = eval(input("Enter an array : "))
v = float(input("Enter number to find : "))
find_in_list(L, v )
