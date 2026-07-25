#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Uses MySQLdb; SQL injection safe; results sorted by cities.id.
"""

import MySQLdb
import sys


def main():
    """Main function: connects to DB and retrieves cities of a given state."""
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cur = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    if not cities:
        print()
    elif len(cities) == 1:
        print(cities[0])
    else:
        print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
