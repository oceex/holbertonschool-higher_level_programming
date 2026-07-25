#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql_username>
<mysql_password> <db_name> <state_name>
Uses MySQLdb; SQL injection safe; results sorted by cities.id.
"""

import MySQLdb
import sys


def main():
    """Connect to the DB, fetch cities for the given
     state, and print them comma separated."""
    if len(sys.argv) != 5:
        return

    user, passwd, dbname, state_name = (sys.argv[1], sys.argv[2],
                                        sys.argv[3], sys.argv[4])

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=passwd, db=dbname,
                           charset="utf8")
    cur = conn.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Extract names and print as a single comma-separated line
    names = [row[0] for row in rows]
    print(", ".join(names))

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
