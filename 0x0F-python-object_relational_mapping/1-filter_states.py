#!/usr/bin/python3
"""
list all states starting with `N` from database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv, stderr


def filterStates():
    """List only states in the table `states` which start with an `N`"""

    err_msg = "usage: {} <username> <password> <db_name>\n".format(argv[0])
    if len(argv) != 4:
        stderr.write(err_msg)
        return

    username, password, db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8",
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    db.close()


if __name__ == "__main__":
    filterStates()
