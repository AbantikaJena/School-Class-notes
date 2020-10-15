# WAP to count and display number of times the value is present in the list ID.
# Eg. ID=[5,7,5,8,9,4,5]
#the program should display
#5 found 3 times
def count_elements_in_ID(L):
    L2=[]
    for i in ID:
        if i not in L2:
            L2.append(i)
    x = [ID.count(elements) for elements in L2]
    for i in range(len(L2)):
        print(L2[i], " found ", x[i], " times.")

ID = eval(input("Enter an array : "))
count_elements_in_ID(ID)
