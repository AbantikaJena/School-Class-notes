# wap to create a 2d array marks scoring 3 diff. student 5 diff. marks and 10 grace marks to each student print marts in row and column format

Marks = [[56,43,43,65,54],[65,54,76,34,54],[48,67,54,56,31]]
for i in range (0,3):
    print("Student %d:"%int(i+1),end=" ")
    for j in range(0,5):
        Marks[i][j] = Marks[i][j] + 10
        print(Marks[i][j],end=" ")
    print()
