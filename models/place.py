#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False))

if storage_type == "db":
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", back_populates="place_amenities",
                                 secondary=place_amenity, viewonly=False)
else:
    class Place(BaseModel):
        """ A place to stay to BaseModel"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            objs = [x for x in storage.all().values()
                    if x.__class__ == "Review" and x.place_id == self.id]
            return objs

        @property
        def amenities(self):
            from models import storage
            objs = [x for x in storage.all().values()
                    if x.__class__.__name__ == "Amenity"
                    and x.id in self.amenity_ids]
            return objs
            """self.amenity_ids = storage.all(Amenity)
            return self.amenity_ids"""

        @amenities.setter
        def amenities(self, obj):
            if obj.__clas__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
