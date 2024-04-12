#!/usr/bin/python3
"""Defines the state class."""
import models
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv



class State(BaseModel, Base):
    """Represents a state for a MySQL database.


    Inherits from SQLAlchemy Base and links to the MySQL table states.


    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
