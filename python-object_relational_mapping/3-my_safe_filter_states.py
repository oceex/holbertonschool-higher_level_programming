#!/usr/bin/python3
"""Module that lists all states from the database hbtn_0e_0_usa
matching a name given by the user, safe from MySQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to a MySQL server and safely display all states whose
    name matches the argument given by the user, ordered by states.id.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name, charset="utf8")
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
