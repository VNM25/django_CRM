import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root',

	)


#prepare a cursor object

cursorObject = dataBase.cursor(buffered = True)

#create a Database
cursorObject.execute("CREATE DATABASE data")

print("ALL Done")