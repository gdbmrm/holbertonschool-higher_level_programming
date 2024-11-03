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
    my_state = sys.argv[4]
    cur.execute(
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s"
        "ORDER BY cities.id ASC;", (my_state,))

    query_rows = cur.fetchall()

    all_cities = [city[0] for city in query_rows]
    print(", ".join(all_cities))

    cur.close()
    database.close()
