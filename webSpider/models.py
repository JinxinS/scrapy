# -*- coding: utf-8 -*-
import sys
reload(sys)   
sys.setdefaultencoding('utf8')  
from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_movie_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Movie(DeclarativeBase):
        __tablename__="Library"
        id = Column(Integer, primary_key=True)
        name =Column('name',String)
        link = Column('link', String, nullable=True)

