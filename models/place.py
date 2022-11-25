#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False)
)


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

    @property
    def reviews(self):
        from models import storage
        objs = [x for x in storage.all().values() if x.__class__ == "Review" and x.place_id == self.id]
        return objs

    @property
    def amenities(self):
        from models import storage
        objs = [x for x in storage.all().values() \
                if x.__class__ == "Amenity" \
                and x.id in self.amenity_ids]
        return objs

    @amenities.setter
    def amenities(self, obj):
        if obj.__clas__ == "Amenity":
            self.amenity_ids.append(obj.id)
