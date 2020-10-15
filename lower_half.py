# write a program to print the lower-half() which takes a two dimentional array A, with N rows and N column as arguments and print the lower half of the matrix.

def lower_half(A):
    k=0
    for i in range(len(A)):
        j=0
        while (j<=k):
            print(A[i][j],end=" ")
            j=j+1
        print()
        k=k+1

A = [[1,2,3],[4,5,6],[7,8,9]]
lower_half(A)
    
        
