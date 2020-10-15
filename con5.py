import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("insert into student1 values(1,'pooja',21,'shimla',390)")
mydb.commit()
print(mycursor.rowcount,"Record inserted")
