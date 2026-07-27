#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(usr, pas, db):
    """" script that adds the State object "Louisiana" to db """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
