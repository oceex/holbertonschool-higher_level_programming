#!/usr/bin/python3
"""Lists all cities from a MySQL database, ordered by cities.id."""
import sys
import MySQLdb


def list_cities(username, password, database):
    """Connect to the MySQL server and print every city, sorted by id."""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name "
                   "FROM cities "
                   "ORDER BY cities.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.stderr.write(
            "Usage: {} <mysql_username> <mysql_password> <database_name>\n"
            .format(sys.argv[0])
        )
        sys.exit(1)

    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
