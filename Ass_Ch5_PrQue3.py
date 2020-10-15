#Assignment Ch5 File Handling
#Que 3
#From binary files give details about salary ε[20000,40000]
f1=open("Employee.dat", "r")
f2=open("Employee_new.dat", "w")
data=f1.read(8)
t=""
print("Details of Employment:-")
while data != '':
    try:
        plaintext = chr(int(data,2))
        print(plaintext,end="")
        data = f1.read(8)
        t+=plaintext
    except:
        break
f2.write(t)
f2.close()
print("\n")
print("Employee with salary between 20000 & 40000:-","\n")
f3 = open("Employee_new.dat", "r") 
x = f3.readline()  
while (x):
    i=x.split(":")
    if int(i[2])>=20000 and int(i[2])<=40000:  
        print (x) 
    x=f3.readline()
f1.close()
f3.close()
