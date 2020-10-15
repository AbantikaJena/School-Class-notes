# Make pattern
# 0 1 2 3
# 1 2 3 0
# 2 3 0 0
# 3 0 0 0
A =[[0,1,2,3]]
k=3
for i in range(4):
    for j in range(4):
        if k>=j :
            print(A[0][i+j],end=" ")
        else:
            print("0",end=" ")
    print()
    k=k-1




