#!/usr/bin/python3
"""Defines the state class."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import models
import shlex
import os


store = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """This is the class for State
    Attributes: 
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if store == 'db':
        cities = relationship('City', backref='state', cascade='all, 
                delete, delete-orphan')

        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list.append(city)
            return list
