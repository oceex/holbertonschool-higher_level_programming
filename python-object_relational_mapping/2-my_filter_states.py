#!/usr/bin/python3
"""Module that lists all states from the database hbtn_0e_0_usa
matching a name given by the user, using MySQLdb.
"""
import MySQLdb
import sys


def main(usr, pas, db, arg):
    """" takes in an argument and displays all values in the states table  """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=pas,
                         db=db, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' "
                "ORDER BY id ASC".format(arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
