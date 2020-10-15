import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("alter table student1 add(marks integer)")
mycursor.execute("desc student1")
for x in mycursor:
    print(x)
