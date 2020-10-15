# name of function Arrayformat(num)

def Arrayformat(num):
    k=0
    for i in range(len(A)):
        j=0
        for i2 in range(3):
            if j<=2 :
                print(A[0][j],end=" ")
                j=j+1
            else:
                print("0",end=" ")
        print()
        k=k+1

A = [[1,2,3]]
Arrayformat(A)
    
