#!/usr/bin/python3
"""Module that defines a db storage"""
from sqlalchemy import create_engine
import os


class DBStorage:
    """Class tha defines a storage of models in db format"""
    __engine = None
    __session = None

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
            """
            a = Metadata(link=self.__engine)
            a.drop_all()
            """
            """DROP ALL TABLES"""

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {k: v for k, v in DBStorage.__session.items() \
                    if type(v) == cls}
        return DBStorage.__session

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes input object from storage"""
        if obj is not None:
            self.all().pop(obj.to_dict()['__class__'] + '.' + obj.id, None)

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(DBStorage.__session)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

