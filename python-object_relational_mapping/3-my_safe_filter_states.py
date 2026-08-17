#!/usr/bin/python3
"""
Script that lists all states matching a name from the database
hbtn_0e_0_usa, safe from MySQL injection.
"""
import MySQLdb
import sys


def main(usr, pas, db, arg):
    """" takes in arguments and displays all values in the states table """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=pas,
                         db=db, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s "
                "ORDER BY id ASC", (arg,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
