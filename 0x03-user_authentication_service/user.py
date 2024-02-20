#!/usr/bin/env python3
"""Main file for SQLAlchemy model declaration"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Create a base class for declarative class definitions
Base = declarative_base()

class User(Base):
    """SQLAlchemy model for the 'users' table"""
    __table__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
