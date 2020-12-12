#!/usr/bin/python3
""" script that use a ForeignKey
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    user = argv[1]
    passw = argv[2]
    nm_db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, nm_db))
    Session = sessionmaker(bind=engine)
    session = Session()
    join = session.query(City, State).filter(State.id == City.state_id).all()
    for ct, st in join:
        print("{}: ({}) {}" .format(st.name, ct.id, ct.name))
    session.close()
