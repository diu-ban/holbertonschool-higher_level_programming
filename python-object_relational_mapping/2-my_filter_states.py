#!/usr/bin/python3
"""
Script that takes in an argument
and displays all values in the
states table of hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./2-my_filter_states.py
    <mysql username> <mysql password> <database name> <statename>

This script connects to a MySQL server
running on localhost at port 3306
and retrieves all states from
the `states` table, displaying them in
ascending order by `id`.
"""

import MySQLdb
import sys


def list_states(username, password, db_name, state_name):
    """
    Connects to a MySQL database and lists all states
    name matches the argument in ascending order by id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name pattern
    """
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name, port=3306
        )
    cursor = db.cursor()

    query = ("SELECT * FROM states WHERE BINARY name LIKE {} ORDER BY id".format(state_name))
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    """
    Main execution block that retrieves
    command-line arguments and calls list_states.
    """
    list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
