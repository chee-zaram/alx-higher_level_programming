#!/usr/bin/python3
"""
Defines a class `State` and instance `Base`
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines `State` which inherits from `Base`

    Attributes:
        __tablename__ (str): name of the table in database
        id (int): primary key to identify the row in the table
        name (str): name of the of row in the table
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __repr__(self):
        """returns a reproducible representation of the `State` object"""
        return "State(id={}, name='{}')".format(self.id, self.name)
