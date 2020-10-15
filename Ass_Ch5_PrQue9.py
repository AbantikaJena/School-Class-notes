# Assignment Ch5 File Handling

# Que 9

# Print just the last line of a text file

def readfile(x):
    f=open(x,"r")
    rn=0
    for i in f.readlines(): # find serial no of last line
        rn+=1
    f.close()
    f=open(x,"r")
    rl=0
    for j in f.readlines(): # find last line
        rl+=1
        if rl==rn:
            print("Last line : ",j)
x=input("Enter  file : ")
readfile(x)
