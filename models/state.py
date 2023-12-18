#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tabename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter for cities"""
        return [city for city in self.cities if city.state_id == self.id]
