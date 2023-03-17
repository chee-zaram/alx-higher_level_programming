#!/usr/bin/python3
"""
Defines a class `State` and instance `Base`
"""

from sqlalchemy import Integer, String, Column, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines `State` which inherits from `Base`

    Attributes:
        __tablename__ (str): name of the table in database
        id (int): primary key to identify the row in the table
        name (str): name of the of row in the table
    """

    __tablename__ = 'states'

    id = Column(Integer, Sequence('user_id_seq'),
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
