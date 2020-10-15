# deleting record through python interface

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("delete from student1 where rollno = 1")
mydb.commit()
print(mycursor.rowcount,"Recod(s) Deleted")
