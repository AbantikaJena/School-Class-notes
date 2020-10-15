num=[]
def selectionsort(num):
    n=len(num)
    for i in range(n-1):
        smallindex=i
        for j in range(i+1,n):
            if num[j]<num[smallindex]:
                smallindex = j
        if smallindex!=i:
            temp=num[i]
            num[i]=num[smallindex]
            num[smallindex]=temp
L = [10,51,2,18,4,31,13,5,23,64,29]
selectionsort(L)
print("sorted List")
for i in range(0,len(L)):
    print(L[i],end=" ")
