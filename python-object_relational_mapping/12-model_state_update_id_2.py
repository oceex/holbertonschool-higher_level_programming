#!/usr/bin/python3
"""
Changes the name of the State with id = 2 to 'New Mexico'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(usr, pas, db):
    """" Changes the name of the State with id = 2 to 'New Mexico'. """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    (session.query(State).filter(State.id == 2)
     .update({State.name: "New Mexico"}))
    session.commit()

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
