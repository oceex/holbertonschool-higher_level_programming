#!/usr/bin/python3
"""Script that lists all cities of a state from the database hbtn_0e_4_usa."""
import MySQLdb
import sys


def main(user, password, database, state):
    """Connect to MySQL and print all cities belonging to the given state."""
    mydb = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=password, db=database)
    mycur = mydb.cursor()
    mycur.execute("SELECT cities.name FROM cities "
                  "INNER JOIN states ON cities.state_id = states.id "
                  "WHERE states.name = %s "
                  "ORDER BY cities.id ASC", (state,))
    cities = [row[0] for row in mycur]
    print(", ".join(cities))
    mycur.close()
    mydb.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
