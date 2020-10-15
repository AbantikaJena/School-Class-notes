#Assignment Ch5 File Handling

#Que 4

# Count the number of times “my” 

def countmy():
    f=open("DATA.txt")
    c=0
    for i in f.read().split():
        if "my"==i:
            c+=1
    print("my occurs ",c," time/s.")
countmy()
