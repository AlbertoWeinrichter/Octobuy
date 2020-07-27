from functools import wraps

from flask import make_response
from flask_jwt_extended import get_jwt_claims, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt import DecodeError, ExpiredSignatureError
from source.conf.extensions import jwt_security


@jwt_security.user_claims_loader
def load_roles(identity):
    return identity["roles"]


def role_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                claims = get_jwt_claims()
                if role in claims or role == "admin":
                    return f(*args, **kwargs)
                else:
                    response = {"message": "You don't have enough permissions"}
                    return make_response(response), 401
            except DecodeError as e:
                print(e)
                response = {"message": "Malformed token"}
                return make_response(response), 422

            except NoAuthorizationError as e:
                print(e)
                response = {"message": "Request had no Authorization token"}
                return make_response(response), 403

            except ExpiredSignatureError as e:
                print(e)
                response = {"message": "Token outdated"}
                return make_response(response), 412

        return decorated_function

    return decorator
