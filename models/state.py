#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if storage_type == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete")
else:
    class State(BaseModel):
        """ State class to BaseModel"""
        name = ""

        @property
        def cities(self):
            from models import storage
            objs = [x for x in storage.all().values()
                    if type(x) == City and x.state_id == self.id]
            return objs
