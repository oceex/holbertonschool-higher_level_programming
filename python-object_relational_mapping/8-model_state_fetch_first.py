#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
<db_name>
If no state is found, prints "Nothing".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def main(usr, pas, db):
    """Connect to the DB and print the first State by id or 'Nothing'
     if empty."""

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pas, db),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
