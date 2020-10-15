# Make pattern
# 1 2 3
# 1 2 0
# 1 0 0
def upper_half(num):
    k=2
    for i in range(3):
        for j in range (3):
            if k>=j :
                #print("k:",k)
                print(A[0][j],end=" ")
            else:
                print("0",end=" ")
        print()
        k=k-1
A = [[1,2,3]]
upper_half(A)
