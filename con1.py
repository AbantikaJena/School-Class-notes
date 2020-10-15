import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507")
mycursor = mydb.cursor()
mycursor.execute("create database school")

          
