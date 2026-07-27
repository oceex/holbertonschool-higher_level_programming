#!/usr/bin/python3
"""Lists all City objects from hbtn_0e_101_usa, using the state
relationship and a single query, sorted ascending by cities.id."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main(usr, pas, db):
    """" script that lists all City objects from db """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
