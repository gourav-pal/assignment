import sqlite3
import csv

con=sqlite3.connect('example.sqlite')
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS example')
cur.execute('''
CREATE TABLE "example"(
       "col_1" TEXT,
       "col_2" TEXT,
       "col_3" TEXT,
       "col_4" TEXT
       
       )
''')

fname=input("enter the csv file name") #user will enter
if len(fname)<1 : fname="Book1.csv" #here we have taken file name by default
with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        col_1=row[0]
        col_2=row[1]
        col_3=row[2]
        col_4=row[3]
        
        cur.execute('''INSERT INTO example(col_1,col_2,col_3,col_4)VALUES(?,?,?,?)''',(col_1,col_2,col_3,col_4))
        con.commit
