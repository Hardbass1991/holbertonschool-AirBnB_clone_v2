#!/usr/bin/python3
"""Module that defines a db storage"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

metadata_obj = MetaData()


class DBStorage:
    """Class tha defines a storage of models in db format"""
    __engine = None
    __session = None

    clss = [User, Place, State, City, Amenity, Review]

    def __init__(self):
        dialect = "mysql"
        driver = "mysqldb"
        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(dialect + "+" + driver + "://" + 
                username + ":" + password + "@" + host + "/" + database,
                pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            metadata_obj.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        session = self.__session()
        d = {}
        A = list(self.clss)
        if (cls is not None and cls in self.clss) or cls is None:
            if cls is not None:
                A = [cls]
            for x in A:
                results = session.query(x)
                for result in results:
                    d[result.__class__.__name__ + "." + result.id] = result
            return d

    def new(self, obj):
        """Adds new object to storage dictionary"""
        session = self.__session()
        session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        session = self.__session()
        session.commit()

    def delete(self, obj=None):    
        """Deletes input object from storage"""
        if obj is not None and type(obj) in self.clss:
            session = self.__session()
            session.query(type(obj)).filter(type(obj).id == obj.id).delete()

    def reload(self):
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(session_factory)
