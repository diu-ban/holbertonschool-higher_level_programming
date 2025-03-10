#!/usr/bin/python3
"""
Module that contains the class definition for State
and connects it to the MySQL database table.
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    State class that maps to the 'states' table in MySQL.
    It inherits from Base and defines columns `id` and `name`.
    """
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key= True,
                autoincrement= True,
                nullable= False)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    """
    Script that creates a connection to the MySQL database
    and creates the 'states' table based on the State class.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
        )
    Base.metadata.create_all(engine)
