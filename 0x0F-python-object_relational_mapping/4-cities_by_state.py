#!/usr/bin/python3
"""Lists all cities from database `hbtn_0e_4_usa`"""

import MySQLdb
from sys import argv, stderr


def getCities():
    """Gets all the cities in the database `hbtn_0e_4_usa`"""

    err_msg = "usage: {} <uname> <passwd> hbtn_0e_4_usa\n".format(argv[0])
    if len(argv) != 4:
        stderr.write(err_msg)
        return

    uname, password, db_name = argv[1], argv[2], argv[3]
    # if db_name != "hbtn_0e_4_usa":
    #     stderr.write("invalid database name, should be 'hbtn_0e_4_usa'")
    #     return

    db = MySQLdb.connect(
        host="localhost",
        user=uname,
        passwd=password,
        db=db_name,
        charset="utf8",
        port=3306
    )

    q = "SELECT cities.id, cities.name, states.name FROM cities JOIN states \
    ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur = db.cursor()
    cur.execute(q)
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    getCities()
