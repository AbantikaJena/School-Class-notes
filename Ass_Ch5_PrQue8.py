# Assignment Ch5 File Handling

# Que 8

# display all records with line/record number

def readfile(x):
    f=open(x,"r")
    rn=0
    for i in f.readlines():
        rn+=1
        print(rn,i)
x=input("Enter the file name : ")
readfile(x)
