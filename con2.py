import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "school")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student1(Rollno integer Primary key,Name Varchar(15),age integer,city char(8))")
