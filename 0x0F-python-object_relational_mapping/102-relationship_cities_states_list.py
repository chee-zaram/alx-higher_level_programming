#!/usr/bin/python3
"""
Queries `hbtn_0e_101_usa` MySQL database through localhost port 3306
usage: <script> <username> <password> <database_name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sys import argv, stderr


def listAllCities():
    """Lists all `City` objects

    Format:
        <city_id>: <city_name> -> <state_name>
    """

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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == "__main__":
    listAllCities()
