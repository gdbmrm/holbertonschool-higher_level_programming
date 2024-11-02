#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )

    cur = database.cursor()
    my_state = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (my_state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    database.close()
