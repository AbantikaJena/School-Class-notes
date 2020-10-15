# where clause
import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("select name, marks,age from student1 where city ='shimla' ")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)
