#Create table cricketer(cid, cname, match, run) and insert 8 players records. Print player records with average. and write this data into player.csv file. Do all this task from python.
import sqlite3 as sq
con=sq.connect("C:\\Users\\MCA\\Desktop\\23BCA270\\sqlite-tools-win-x64-3460000\\data\\player.db")
cur=con.cursor()
q="create table if not exists cricketerr(cid, cname, match, run)"
cur.execute(q)
con.commit
cur=con.cursor()
cur.execute("insert into cricketerr values(1,'Rohit Sharma',250,18000)")
cur.execute("insert into cricketerr values(2,'Sachin Tendulkar',452,18426)")
cur.execute("insert into cricketerr values(3,'Rahul Dravid',286,13228)")
cur.execute("insert into cricketerr values(4,'Sunil Gavaskar',217,10112)")
cur.execute("insert into cricketerr values(5,'VVS Laxman',134,8781)")
cur.execute("insert into cricketerr values(6,'Virender Sehwag',180,8586)")
cur.execute("insert into cricketerr values(7,'Dilip Vengsarkar',116,6868)")
cur.execute("insert into cricketerr values(8,'Kapil Dev',184,5248)")
con.commit()
cur.execute("select cname,match,run,(run * 2.0/match)as average from cricketerr")
rec=cur.fetchall()
print(rec)
con.commit()
#write this data into player.csv file
import csv
player=[
        ('Rohit Sharma', 250, 18000, 144.0),
        ('Sachin Tendulkar', 452, 18426, 81.53097345132744),
        ('Rahul Dravid', 286, 13228, 92.5034965034965),
        ('Sunil Gavaskar', 217, 10112, 93.19815668202764),
        ('VVS Laxman', 134, 8781, 131.0597014925373),
        ('Virender Sehwag', 180, 8586, 95.4),
        ('Dilip Vengsarkar', 116, 6868, 118.41379310344827),
        ('Kapil Dev', 184, 5248, 57.04347826086956)
]
with open('D:/23BCA270/sqlite3/data/player.csv','w') as f:
    w=csv.writer(f)
    w.writerows(player)
with open('D:/23BCA270/sqlite3/data/player.csv','r') as f:
    r=csv.reader(f)
    for row in r:
        print(row)
    
