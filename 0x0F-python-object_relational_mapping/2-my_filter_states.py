#!/usr/bin/python3
"""
list all states matching user input in database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv, stderr


def getState():
    """list all states matching user input in database `hbtn_0e_0_usa`"""

    err_msg = "usage: {} <username> <passwd> <db_name> <state_name>\n".format(
        argv[0])

    if len(argv) != 5:
        stderr.write(err_msg)
        return

    username, password, db_name, state = argv[1], argv[2], argv[3], argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8",
        port=3306
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(state)

    cur.execute(query)
    result = cur.fetchall()

    for row in result:
        print(row)

    db.close()


if __name__ == "__main__":
    getState()
