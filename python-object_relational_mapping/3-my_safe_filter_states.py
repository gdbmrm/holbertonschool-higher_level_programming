#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb, sys

database = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa",
    charset="utf8")


cur = database.cursor()
my_state = sys.argv[4]
query = "SELECT * FROM states WHERE name = %s"
cur.execute(query, (my_state,))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
database.close()
