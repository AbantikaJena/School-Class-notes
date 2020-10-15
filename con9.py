# updating record through python interface

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("update student1 set age = 18 where name = 'vijay' ")
mydb.commit()
print(mycursor.rowcount,"Recod(s) updated")
