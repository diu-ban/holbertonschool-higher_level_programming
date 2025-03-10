#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.

Usage:
    ./4-cities_by_state <mysql username> <mysql password> <database name>

This script connects to a MySQL server running on localhost at port 3306
and retrieves all states from the `states` table, displaying them in
ascending order by `id`.
"""

import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Connects to a MySQL database and lists all cities
    in ascending order by id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
    """
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name, port=3306
        )
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id"
        )

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    db.close()


if __name__ == '__main__':
    """
    Main execution block that retrieves
    command-line arguments and calls list_cities.
    """
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
