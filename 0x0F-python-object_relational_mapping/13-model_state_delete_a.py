#!/usr/bin/python3
""" script that delete all State objects that contain the letter a
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    nm_dt = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, nm_dt))
    Session = sessionmaker(bind=engine)
    session = Session()
    consulta = session.query(State).filter(State.name.ilike('%a%'))
    for instance in consulta:
        session.delete(instance)
    session.commit()
    session.close()
