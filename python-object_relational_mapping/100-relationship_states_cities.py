#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
in the database hbtn_0e_100_usa, using the cities relationship.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main(usr, pas, db):
    """" Creates the State 'California' with the City 'San Francisco' """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, pas, db),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_ca = State(name="California")
    city_sf = City(name="San Francisco")

    state_ca.cities.append(city_sf)

    session.add(state_ca)
    session.commit()

    session.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
