#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(usr, pas, db):
    """" Deletes all State objects with a name containing the letter 'a' """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session=False)
    session.commit()

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
