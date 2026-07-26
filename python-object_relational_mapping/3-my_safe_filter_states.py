#!/usr/bin/python3
"""Script that lists all states matching a name from the database
hbtn_0e_0_usa, safe from MySQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to MySQL server and display states matching the given name.

    Takes 4 arguments: mysql username, mysql password, database name
    and the state name to search for. The query is parameterized to
    protect against SQL injection.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s "
                "ORDER BY id ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
