# Assignment Ch5 File Handling

# Que 11

# Display words which are less than 4 characters

def displaywords():
    c = 0
    f = open("POEM.txt")
    for w in f.read().split():
        if len(w)<4:
            c+=1
            print(c ," : ", w)
    print("No of words less than 4 characters : ",c)
    f.close()
displaywords()
