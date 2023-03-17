#!/usr/bin/python3
"""
Queries `hbtn_0e_100_usa` MySQL database through localhost port 3306
usage: <script> <username> <password> <database_name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sys import argv, stderr


def createCaliSanF():
    """Create `State` object `California` with `City` object `San Francisco`"""

    if len(argv) != 4:
        stderr.write("usage: {} <uname> <passwd> <db>\n".argv[0])
        return

    uname, password, db_name = argv[1], argv[2], argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, password, db_name)

    engine = create_engine(db_url, pool_pre_ping=True, echo=False)
    Base.metadata.create_all(engine, checkfirst=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()


if __name__ == "__main__":
    createCaliSanF()
