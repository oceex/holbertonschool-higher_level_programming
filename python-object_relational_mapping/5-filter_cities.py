#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""
import sys
import MySQLdb


def filter_cities(username, password, database, state_name):
    """Print every city belonging to state_name, sorted by cities.id."""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    connection.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])