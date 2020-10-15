# wap to interchage column from 1 to last

def swapping_rows(A):
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][-j-1]=A[i][j]
            print(A[i][j],end=" ")
        print()
        

A = [[1,2,3],[4,5,6],[7,8,9]]
swapping_rows(A)
