#!/usr/bin/python3
"""This is the DB storage class"""


class DBStorage:
    """This class serializes instances to a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        from models.base_model import Base
        from sqlalchemy import create_engine
        from os import getenv
        # from sqlalchemy.orm import sessionmaker # not used

        hb_env = getenv("HBNB_ENV")
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                 password, host, database),
            pool_pre_ping=True,
        )
        # if getenv("HBNB_ENV") == "test":
        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.base_model import Base, BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine

        if cls is None:
            classes = [State, City, User, Place]
            objs = []
            for c in classes:
                objs += self.__session.query(c).all()
        else:
            objs = self.__session.query(cls).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database
        session"""
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place

        from models.review import Review
        from models.amenity import Amenity
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.orm import scoped_session

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
        # Session = scoped_session(
        #     sessionmaker(bind=self.__engine, expire_on_commit=False)
        # )
        # self.__session = Session()
