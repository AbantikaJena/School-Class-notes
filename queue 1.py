# implementation of stack using list


q=[]
c="y"
while (c=="y"):
    print("1.INSERT")
    print("2.DELETE")
    print("3.DISPLAY")
    print("1.EXIT")
    choice = int(input("Enter your choice"))
    if (choice==1):
        a= int(input("Enter any number"))
        q.append(a)
    elif (choice==2):
        if (q==[]):
            print("queue is empty")
        else:
            print("deleted element is :",q.pop(0))
    elif (choice==3):
        l=len(q)
        for i in range(0,l): # to display first to last
            print(q[i])
    elif (choice==4):
        quit()

    else:
        print("wrong choice")
    c=input("Do you want to continue or not")
