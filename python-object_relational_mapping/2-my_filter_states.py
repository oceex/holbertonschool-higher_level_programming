#!/usr/bin/python3
"""Module that lists all states with a name matching a user-provided
argument from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to a MySQL server and print states matching sys.argv[4]."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
ORDER BY states.id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
