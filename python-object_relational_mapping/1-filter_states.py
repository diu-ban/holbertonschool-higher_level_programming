#!/usr/bin/python3
"""
Script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states <mysql username> <mysql password> <database name>

This script connects to a MySQL server running on localhost at port 3306
and retrieves all states from the `states` table, displaying them in
ascending order by `id`.
"""

import MySQLdb
import sys


def list_N_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states
    begin with "N" in ascending order by id.

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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    """Main execution block that retrieves command-line arguments and calls list_states."""
    list_N_states(sys.argv[1], sys.argv[2], sys.argv[3])
    