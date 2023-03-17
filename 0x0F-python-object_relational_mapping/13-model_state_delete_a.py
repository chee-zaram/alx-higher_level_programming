#!/usr/bin/python3
"""
Module to connect to a database `hbtn_0e_6_usa` and query `State` objects
It queries a MySQL database on `localhost` port `3306`
usage: <script> <username> <password> <database>
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stderr


def deleteAllWitha():
    """deletes all `State` objects with `name` attribute having letter `a`"""

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

    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    deleteAllWitha()
