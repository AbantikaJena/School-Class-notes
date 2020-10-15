# implementation of stack using list

def choice1(s):
    a= int(input("Enter any number"))
    s.append(a)

def choice2(s):
    if (s==[]):
        print("Stack is empty")
    else:
        print("deleted element is :",s.pop())

def choice3(s):
    l=len(s)
    for i in range(l-1,-1,-1): # to display last element to the first
        print(s[i])

def mainfun():
    s=[]
    c="y"
    while (c=="y"):
        print("1.PUSH")
        print("2.POP")
        print("3.DISPLAY")
        choice = int(input("Enter your choice"))
        if (choice==1):
            choice1(s)
        elif (choice==2):
            choice2(s)
            
        elif (choice==3):
            choice3(s)
        else:
            print("wrong choice")
        c=input("Do you eant to continue or not")
mainfun()
