#!/usr/bin/python3
"""
Module to connect to a database `hbtn_0e_14_usa` and query objects
It queries a MySQL database on `localhost` port `3306`
usage: <script> <username> <password> <database>
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stderr


def printAllCities():
    """Print all `City` objects in the database"""

    if len(argv) != 4:
        stderr.write(
            "usage: {} <username> <password> <database>\n".format(argv[0]))
        return

    uname, password, db_name = argv[1], argv[2], argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, password, db_name)

    engine = create_engine(db_url, pool_pre_ping=True, echo=False)

    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    printAllCities()
