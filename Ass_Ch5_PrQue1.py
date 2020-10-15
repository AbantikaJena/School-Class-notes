#Assignment Ch5 File Handling

#Que 1

# Write multiple lines of text contents into a text file 

f=open("daynote.txt","w")
f.write("Ass. of School.\n")
f.write("Mon-Eng\n")
f.write("Tue-Phy\n")
f.write("Wed-C.Sc.\n")
f.write("Thu-Chem.\n")
f.write("Fri-Maths.")
f.close()
print("Task Done!!!")
