#!/usr/bin/python3
"""
Script that lists all State
objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)

    for state in session.query(State).filter_by(State.name.ilike('%a%')).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
    
    session.close()
