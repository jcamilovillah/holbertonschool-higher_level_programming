#!/usr/bin/python3
""" create a class called Statethat inherit from Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base

Base = declarative_base()


class City(Base):
    """create table"""
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
