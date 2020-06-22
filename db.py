import sqlite3
import csv

con=sqlite3.connect('exoplanet.sqlite')
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS exoplanet')
cur.execute('''
CREATE TABLE "exoplanet"(
       "id" TEXT,
       "name" TEXT
       )
''')

fname=input("enter")
if len(fname)<1 : fname="Book1.csv"
with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        id=row[0]
        name=row[1]
        cur.execute('''INSERT INTO exoplanet(id,name)VALUES(?,?)''',(id,name))
        con.commit
