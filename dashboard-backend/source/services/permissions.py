from flask import make_response
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_claims
)

from source.conf.extensions import jwt_security


@jwt_security.user_claims_loader
def load_roles(identity):
    return identity["roles"]


from functools import wraps


def role_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if role in claims or role == "admin":
                return f(*args, **kwargs)
            else:
                response = {
                    'message': "You don't have enough permissions",
                }
                return make_response(response), 200

        return decorated_function

    return decorator
