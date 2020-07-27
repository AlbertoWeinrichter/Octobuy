# -*- coding: utf-8 -*-
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
flask_static_digest = FlaskStaticDigest()
jwt_security = JWTManager()
