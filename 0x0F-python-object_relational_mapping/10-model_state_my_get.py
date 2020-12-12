#!/usr/bin/python3
""" prints the State object with the name passed as argument
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    nm_dt = argv[3]
    search = argv[4]
    consult = False
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, nm_dt))
    Session = sessionmaker(bind=engine)
    session = Session()
    consulta = session.query(State).filter(State.name == search)
    for instance in consulta:
        print("{}".format(instance.id))
        consult = True
    if consult is False:
        print("Not found")
    session.close()
