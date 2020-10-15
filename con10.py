# deleting record at the time of running program

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
nm = input("enter name to be deleted : ")
try:
    mycursor.execute("delete from student1 where name = 'nm' ")
    print(mycursor.rowcount,"Recod(s) deleted")
    mydb.commit()
except:
    mydb.rollback()
mydb.close()
