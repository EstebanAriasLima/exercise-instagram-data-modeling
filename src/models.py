import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False)
    email = Column(String(100), nullable = False)
    biography = Column (String(120), nullable = True)
    post = relationship('Post', backref='user')
    reel = relationship('Reel', backref='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(120), nullable = True)
    video = Column(String(120), nullable = True)

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video = Column(String(120), nullable = False)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(120), nullable = True)
    video = Column(String(120), nullable = True)
    song = Column(String(120), nullable = True)
    text = Column(String(120), nullable = True)

class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    post_id = Column(Integer, ForeignKey('post.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship("Story")
    post = relationship("Post")
    reel = relationship("Reel")
    user = relationship("User")

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key = True)
    post_id = Column(Integer, ForeignKey('post.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship("Story")
    reel = relationship("Reel")
    post = relationship("Post")
    user = relationship("User")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e