#!/usr/bin/python3
"""
Module that contains the class definition for city
and connects it to the MySQL database table.
"""

import sys
from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State

class City(Base):
    """
    City class that maps to the 'cities' table in MySQL.
    It inherits from Base and defines columns `id` and `name`.
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

if __name__ == '__main__':
    """
    Script that creates a connection to the MySQL database
    and creates the 'states' table based on the State class.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
        )
    Base.metadata.create_all(engine)
