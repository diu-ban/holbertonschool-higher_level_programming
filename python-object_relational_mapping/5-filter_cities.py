#!/usr/bin/python3
"""
Script that takes in an argument
and displays all values in the
states table of hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./5-filter_cities +
    <mysql username>
    <mysql password>
    <database name>
    <statename>

This script connects to a MySQL server
running on localhost at port 3306
and retrieves all states from
the `states` table, displaying them in
ascending order by `id`.
"""

import MySQLdb
import sys


def list_cities(username, password, db_name, state_name):
    """
    Connects to a MySQL database and lists all city
    name in a state matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Search pattern
    """
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name, port=3306
        )
    cursor = db.cursor()

    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id"
        )
    cursor.execute(query, (state_name,))

    cities = []
    cities.append(city for city in cursor.fetchall())

    cursor.close()
    db.close()


if __name__ == '__main__':
    """
    Main execution block that retrieves
    command-line arguments and calls list_states.
    """
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
