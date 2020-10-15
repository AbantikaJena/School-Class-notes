#Assignment Ch5 File Handling
#Que 7
# Convert Roman no. into Integer

def roman_into_int(n):
    f=open("Roman no Dic.txt","r")
    import json
    rn = json.loads(f.readline())
    i= 0
    for j in range(len(n)):
        if j > 0 and int(rn[n[j]]) > int(rn[n[j-1]]):
            i += int(rn[n[j]]) - (2*(int(rn[n[j-1]])))
        else:
            i += rn[n[j]]
    print ("No. : ",i)
    f.close()
n= input("Enter An Roman no. : ")
roman_into_int(n)


