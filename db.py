import sqlite3
import csv

con = sqlite3.connect('exam.sqlite') #here we will enter our database name 
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS exam')
cur.execute('''
CREATE TABLE "exam"( 
       "col_1" TEXT,
       "col_2" TEXT,
       "col_3" TEXT,
       "col_4" TEXT

       )
''')                                      #created table for reference


fname = input("enter the csv file name")  # user will enter
x = input("enter table name")             # user will enter
if len(fname) < 1: fname = "Book1.csv"  # here we have taken file name by default
with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    values = []

    for r in csv_reader:
        break
    for row in csv_reader:
        row_values = []
        for i in row:
            row_values.append(i)
        values.append(row_values)

    col_names = ""
    value_times = ""
    for i in r:
        col_names = str(col_names + i + ",")
    l1 = len(r)
    for j in range(0, l1):
        value_times = value_times + "?" + ","
    col_names = col_names[:-1]
    value_times = value_times[:-1]
    

insert_query = '''INSERT INTO {0}({1})VALUES({2})'''.format(x, col_names, value_times)
cur.executemany(insert_query, values)
query1 = 'SELECT * FROM {}'.format(x)
c1 = cur.execute(query1)
print(c1.fetchall())
con.commit

