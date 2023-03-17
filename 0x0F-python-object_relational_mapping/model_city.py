#!/usr/bin/python3
"""
Defines a class `City`
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """Defines `City` which inherits from `Base`

    Represents a table `cities` in MySQL database.

    Attributes:
        __tablename__ (str): name of the table in database
        id (int): primary key to identify the row in the table
        name (str): name of the of row in the table
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
