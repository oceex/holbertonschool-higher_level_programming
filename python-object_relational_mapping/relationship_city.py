#!/usr/bin/python3
"""
Defines the City model for SQLAlchemy ORM mapping to the
cities table.

This module provides:
- City: a mapped class representing the cities table with an
  auto-incrementing integer primary key 'id', a non-null string
  'name' (max 128 characters), and a non-null integer 'state_id'
  foreign key referencing states.id. The 'state' backref (defined
  on State.cities) gives access to the linked State object.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """SQLAlchemy City model mapped to the 'cities' table.

    Attributes:
        id (int): Auto-generated unique integer primary key, not nullable.
        name (str): City name, string up to 128 characters, not nullable.
        state_id (int): Foreign key referencing states.id, not nullable.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
