#!/usr/bin/python3
"""
Defines the State model and Base for SQLAlchemy ORM mapping to the
states table, including a relationship to City.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    SQLAlchemy State model mapped to the 'states' table.

    Attributes:
        id (int): Auto-generated unique integer primary key, not nullable.
        name (str): State name, string up to 128 characters, not nullable.
        cities (list): Relationship to linked City objects; deleting
            this State cascades the delete to all linked cities.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan", order_by="City.id")
