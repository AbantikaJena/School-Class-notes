l1 = [1,2,3,4,5,6,7,8,9]
k=[ele1*ele2 for ele1 in l1 if (ele1-4)>1 for ele2 in l1[:4]]
print(k)
