#!/usr/bin/python3
"""
Module to connect to a database `hbtn_0e_6_usa` and query `State` objects
It queries a MySQL database on `localhost` port `3306`
usage: <script> <username> <password> <database> <state>
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stderr


def printFirstToMatch():
    """print the `id` of the first state to match the input by the user"""

    if len(argv) != 5:
        stderr.write("invalid number of arguments\n")
        return

    uname, password, db_name, state = argv[1], argv[2], argv[3], argv[4]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, password, db_name)

    engine = create_engine(db_url, pool_pre_ping=True, echo=False)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    printFirstToMatch()
