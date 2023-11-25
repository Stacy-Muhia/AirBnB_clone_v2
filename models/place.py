#!/usr/bin/python3
""" Place Module for HBNB project """


from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship('Amenity', secondary=place_amenity,
                viewonly=False, backref='place_amenities')

    user = relationship('User', backref='places')
    cities = relationship('City', backref='places')
