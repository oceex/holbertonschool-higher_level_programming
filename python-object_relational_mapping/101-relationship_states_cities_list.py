#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from hbtn_0e_101_usa, using the cities relationship and a single
query, sorted ascending by states.id and cities.id.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main(usr, pas, db):
    """"  lists all State objects, and corresponding
    City objects, contained in db """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = session.query(City).filter(
            City.state_id == state.id).order_by(City.id).all()
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
