#!/usr/bin/python3
"""Prints the State object with the name passed as argument (argv[4]),
searched safely from argv[3]."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(usr, pas, db, arg):
    """"  prints the State object with the name passed as argument from db """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == arg).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
