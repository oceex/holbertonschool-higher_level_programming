#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
<db_name>
If no state is found, prints "Nothing".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():
    """Connect to the DB and print the first State by id or 'Nothing'
     if empty."""
    if len(sys.argv) != 4:
        return

    user, passwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb: //{user}: {passwd}@localhost/{dbname}",
        pool_pre_ping=True
    )

    session = Session(engine)
    try:
        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
