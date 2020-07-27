import datetime
import datetime as dt
import os
from typing import List
import sqlalchemy_jsonfield

import jwt
from flask_jwt_extended import create_access_token
from flask_login import UserMixin
from source.conf.extensions import bcrypt
from passlib.context import CryptContext
from pydantic import BaseModel, Json
from source.conf.database import (Column, Model, SurrogatePK, db)


class UserSchema(BaseModel):
    id: int
    username: str
    refresh_token: str
    roles: List[str]
    extra_info: Json

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    accessToken: str
    refreshToken: str


class User(UserMixin, SurrogatePK, Model):
    __tablename__ = "users"
    username = Column(db.String(256), unique=True, nullable=False)
    email = Column(db.String(256), unique=True, nullable=False)
    refresh_token = Column(db.LargeBinary(128), unique=True, nullable=False)
    password = Column(db.LargeBinary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    roles = Column(db.ARRAY(db.String(256)))
    extra_info = db.Column(
        sqlalchemy_jsonfield.JSONField(
            enforce_unicode=False
        ),
        nullable=False
    )

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def create_access_token(self, user_id, roles):
        """
        Generates the Access Token
        :return: string
        """
        try:
            payload = {
                'roles': roles,
                'user_id': user_id
            }
            token = create_access_token(
                identity=payload,
                # expires_delta=datetime.timedelta(seconds=30) TODO: change this to couple minutes
                expires_delta = datetime.timedelta(days=30)
            )
            return token
        except Exception as e:
            return e

    def encode_refresh_token(self, user_id):
        """
        Generates the Refresh Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                'iat': datetime.datetime.utcnow(),
                'identity': user_id
            }
            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def decode_access_token(token):
    payload = jwt.decode(
        token,
        os.environ.get('SECRET_KEY'),
        algorithm='HS256'
    )
    return payload


def decode_refresh_token(token):
    payload = jwt.decode(
        token,
        os.environ.get('SECRET_KEY'),
        algorithm='HS256'
    )
    return payload
