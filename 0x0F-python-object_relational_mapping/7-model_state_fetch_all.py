#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{
                           password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

