#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    nm_db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, nm_db))
    Session = sessionmaker(bind=engine)
    session = Session()
    user1 = State(name="Louisiana")
    session.add(user1)
    session.commit()
    print(user1.id)
    session.close()
