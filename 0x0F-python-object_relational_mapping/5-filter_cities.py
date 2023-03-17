#!/usr/bin/python3
"""Uses inputed name of state to list all `cities` of that state
in `hbtn_0e_4_usa`"""

import MySQLdb
from sys import argv, stderr


def citiesOfStates():
    """Uses a given name of a state to list all cities in the state"""

    if len(argv) != 5:
        stderr.write("not enough arguments")
        return

    uname, password, db_name, state = argv[1], argv[2], argv[3], argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=uname,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name=%s
            ORDER BY cities.id ASC;
            """

    cur.execute(query, (state,))
    result = cur.fetchall()

    if result is not None:
        print(', '.join(city_tuple[0] for city_tuple in result))

    cur.close()
    db.close()


if __name__ == "__main__":
    citiesOfStates()
