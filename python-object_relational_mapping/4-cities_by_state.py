#!/usr/bin/python3
"""
Lists all cities from a MySQL database, ordered by cities.id.
"""
import sys
import MySQLdb


def list_cities(username, password, database):
    """ Connect to the MySQL server and print every city with its state.
    Prints one tuple per city as (city.id, city.name, state.name),
    sorted in ascending order by city.id, using a single JOIN query.
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
