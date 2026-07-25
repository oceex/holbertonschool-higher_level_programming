#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

def main(user, password, database, searched):
    """Connect to MySQL and print states whose name matches the searched word"""
    mydb = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=password, db=database)
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM states WHERE STRCMP(name, '{0}') = 0".format(searched))
    for row in mycur:
        print(row)

    mycur.close()
    mydb.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
