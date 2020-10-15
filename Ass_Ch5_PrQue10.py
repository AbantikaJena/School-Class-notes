# Assignment Ch5 File Handling

# Que 10

# Copies text file barring lines starting with “@”

f1=open("source.txt")
f2=open("copy.txt","w")
for i in f1.readlines():
    if i[0]!="@":
        f2.writelines(i)
f2.close()
f1.close()
print("Task Done!!!")
