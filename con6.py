import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("select * from student1")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)
