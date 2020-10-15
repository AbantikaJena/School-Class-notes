# write a program to print the lower-half() which takes a two dimentional array A, with N rows and N column as arguments and print the lower half of the matrix.

def row_multiplication(A):
    
    for i in range(3):
        mul=1
        for j in range(3):
            mul =mul*A[i][j]
        print("Product of row %d=%d"%(i+1,mul))
        

A = [[1,2,3],[4,5,6],[7,8,9]]
row_multiplication(A)
    
