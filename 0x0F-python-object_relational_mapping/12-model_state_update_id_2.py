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


def updateState2():
    """updates the `name` attribute of a `State` object with id == 2"""

    if len(argv) != 4:
        stderr.write("invalid number of arguments\n")
        return

    uname, password, db_name = argv[1], argv[2], argv[3]
    state_id = 2
    state_new_name = "New Mexico"
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, password, db_name)

    engine = create_engine(db_url, pool_pre_ping=True, echo=False)

    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=state_id).first()
    if state_to_update:
        state_to_update.name = state_new_name
    else:
        print("Not found")

    session.commit()
    session.close()


if __name__ == "__main__":
    updateState2()
