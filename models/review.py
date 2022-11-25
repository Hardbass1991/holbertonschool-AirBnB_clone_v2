#!/usr/bin/python3
""" Review module for the HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """
    if storage_type == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")

    else:
        text = ""
        place_id = ""
        user_id = ""
