#!/usr/bin/python3
"""Module to connect to a database `hbtn_0e_6_usa` and list all `State` objects
usage: <script> <username> <password> <database>
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stderr


def listStates():
    """Lists all `State` objects"""

    if len(argv) != 4:
        stderr.write("invalid number of arguments\n")
        return

    uname, password, db_name = argv[1], argv[2], argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, password, db_name)

    engine = create_engine(db_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    listStates()
