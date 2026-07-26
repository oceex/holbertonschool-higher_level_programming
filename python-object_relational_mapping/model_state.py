#!/usr/bin/python3
"""
Defines the State model and Base for SQLAlchemy ORM mapping to the
states table.

This module provides:
- Base: the declarative base used by SQLAlchemy.
- State: a mapped class representing the states table with
an auto-incrementing
  integer primary key 'id' and a non-null string 'name' (max 128 characters).
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """SQLAlchemy State model mapped to the 'states' table.

    Attributes:
        id (int): Auto-generated unique integer primary key, not nullable.
        name (str): State name, string up to 128 characters, not nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
