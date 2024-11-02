#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "ORDER BY cities.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    database.close()
