import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

    def to_dict(self):
        return {}

class Favorite_type(Base):
    __tablename__ = 'favorite_type'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    character_id = Column (Integer, ForeignKey('characters,id')
    character = relationship(Characters)
    


    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    relation_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    favorite_type_id = Column(Integer, ForeignKey('favorite_type.id'))
    favorite_type = relationship(Favorite_type)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
