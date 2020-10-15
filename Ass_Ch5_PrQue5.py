# Assignment Ch5 File Handling

# Que 5

# Display those lines which start with the alphabet ‘P’

def Dispay_line():
    f=open("DIARY.txt")
    for i in f.readlines():
        if i[0]=="P":
            print("Line starts with P : ",i)
    f.close()
Dispay_line()
