# implementation of stack using list


s=[]
c="y"
while (c=="y"):
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    choice = int(input("Enter your choice"))
    if (choice==1):
        a= int(input("Enter any number"))
        s.append(a)
    elif (choice==2):
        if (s==[]):
            print("Stack is empty")
        else:
            print("deleted element is :",s.pop())
    elif (choice==3):
        l=len(s)
        for i in range(l-1,-1,-1): # to display last element to the first
            print(s[i])
    else:
        print("wrong choice")
    c=input("Do you eant to continue or not")
