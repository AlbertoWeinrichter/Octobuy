from typing import List, Optional
from datetime import date

from sqlalchemy import inspect, ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from source.conf.database import (Model, Column, db, SurrogatePK)
from pydantic import BaseModel


class PublicationSchema(BaseModel):
    author: int
    type_of: str
    title: str
    slug: str
    description: Optional[str]
    created_at: Optional[date]
    published_at: Optional[date]
    edited_at: Optional[date]
    cover_image: Optional[str]
    social_image: Optional[str]
    body_html: Optional[str]

    tags: Optional[List[str]]
    summary: Optional[List[str]]


class PublicationListSchema(BaseModel):
    publication_list: List[PublicationSchema]


class Publication(SurrogatePK, Model):
    __tablename__ = "publication"

    author = db.Column(db.Integer(), nullable=False)
    type_of = Column(db.String(256), nullable=False)
    title = Column(db.String(256), unique=True, nullable=False)
    slug = Column(db.String(256), unique=True, nullable=False)
    description = Column(db.String(256), nullable=True)
    comments_count = Column(db.Integer(), default=0)
    reactions_count = Column(db.Integer(), default=0)
    created_at = Column(db.Date())
    published_at = Column(db.Date(), nullable=True)
    edited_at = Column(db.Date(), nullable=True)
    cover_image = Column(db.String(256), nullable=True)
    social_image = Column(db.String(256), nullable=True)
    body_html = Column(db.Text(), nullable=True)
    summary = Column('elements', postgresql.ARRAY(db.String))

    tags = relationship('Tag', secondary='publication_tags')



    def __init__(self, **kwargs):
        db.Model.__init__(self, **kwargs)

    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class Tag(SurrogatePK, Model):
    __tablename__ = 'tag'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    publications = relationship(Publication, secondary='publication_tags')


class PublicationTags(SurrogatePK, Model):
    __tablename__ = 'publication_tags'
    publication_id = Column(
        db.Integer,
        ForeignKey('publication.id'),
        primary_key=True)
    tag_id = Column(
        db.Integer,
        ForeignKey('tag.id'),
        primary_key=True)
