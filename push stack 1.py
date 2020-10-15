def push_val(stack,top):
    ch='y'
    while(ch=='y'):
        val = int(input("Enter value"))
        stack.append(val)
        top=top+1
        ch = input("do you want to enter more value")
        if ch=='n':
            break
    return top
s=[]
top = 0
print(push_val(s,top))
