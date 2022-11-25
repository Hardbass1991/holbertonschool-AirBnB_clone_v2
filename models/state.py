#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="parent",
            cascade="all, delete")

    @property
    def cities(self):
        from models import storage
        objs = [x for x in storage.all().values() if x.__class__ == "City" and x.state_id == self.id]
        return objs

