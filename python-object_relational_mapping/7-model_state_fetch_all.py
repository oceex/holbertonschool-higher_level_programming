#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage: ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <db_name>

Connects to a MySQL server on localhost:3306 using SQLAlchemy, imports State
and Base from model_state, and prints each state in the format "<id>: <name>".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():
    """Connect to the DB, fetch all State objects ordered by id,
     and print them."""
    if len(sys.argv) != 4:
        return

    user, passwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, dbname),
        pool_pre_ping=True
    )

    session = Session(engine)
    try:
        for state in session.query(State).order_by(State.id).all():
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
