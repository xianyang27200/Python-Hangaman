import mysql.connector 

mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='Mysql2020@',
    database='Hangman'
    )
curs = mydb.cursor()
curs.execute("SELECT names FROM list")
list_words = list(curs.fetchall())
#print(list_words[3:-2])

