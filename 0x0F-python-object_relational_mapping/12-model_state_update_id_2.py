#!/usr/bin/python3
""" script that changes the name of a State object from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import update

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    nm_db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, nm_db))
    Session = sessionmaker(bind=engine)
    session = Session()
    consulta = session.query(State).all()
    for instance in consulta:
        if instance.id == 2:
            instance.name = "New Mexico"
    session.commit()
    session.close()
