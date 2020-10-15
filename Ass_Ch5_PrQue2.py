#Assignment Ch5 File Handling

#Que 2

# Displays the number of lines starting with ‘H’

def countH():
    f=open("Para.txt")
    c=0
    for i in f.readlines():
        if i[0]=="H":
            c+=1
    print("No of line start with H : ",c)
    f.close()
countH()
