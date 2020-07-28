from flask import Blueprint, request
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from source.conf.extensions import bcrypt, db
from source.models.user import User, UserLoginSchema, decode_refresh_token
from source.services.permissions import role_required

auth_blueprint = Blueprint("auth", __name__)


class RegisterAPI(MethodView):
    def post(self):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get("email")).first()

        if not user:
            try:
                user = User(
                    username=post_data.get("username"),
                    email=post_data.get("email"),
                    password=post_data.get("password"),
                    roles=["member"],
                    extra_info={},
                    refresh_token=b"",
                )

                db.session.add(user)
                db.session.commit()

                user.refresh_token = user.encode_refresh_token(user.id)

                db.session.add(user)
                db.session.commit()

                response = {"message": "Successfully registered."}
                return response, 201

            except Exception as e:
                print(e)
                response = {"message": "Some error occurred. Please try again."}
                return response, 500
        else:
            response = {"message": "User already exists. Please Log in."}
            return response, 202


class LoginAPI(MethodView):
    def post(self):
        try:
            post_data = request.get_json()
            user = User.query.filter_by(email=post_data.get("email")).first()

            if user and bcrypt.check_password_hash(
                user.password, post_data.get("password")
            ):
                access_token = user.create_access_token(user.id, user.roles)
                user_login_response = UserLoginSchema(
                    accessToken=str(access_token), refreshToken=str(user.refresh_token)
                )

                return user_login_response.dict()
            else:
                response = {"message": "User or password not valid."}
                return response, 404

        except Exception as e:
            print(e)
            response = {"message": "Some error occurred. Please try again."}
            return response, 500


class RefreshAPI(MethodView):
    def post(self):
        try:
            post_data = request.get_json()
            refresh_token = decode_refresh_token(post_data["refreshToken"])

            user = User.query.filter_by(id=refresh_token["identity"]).first()
            access_token = user.create_access_token(user.id, user.roles)
            user_login_response = UserLoginSchema(
                accessToken=access_token, refreshToken=user.refresh_token
            )

            return user_login_response.dict()

        except Exception as e:
            print(e)
            response = {"message": "Some error occurred. Please try again."}
            return response, 500


class LogoutAPI(MethodView):
    @role_required("member")
    def get(self):
        try:
            user = User.query.filter_by(id=get_jwt_identity()["user_id"]).first()
            user.token = ""

            db.session.add(user)
            db.session.commit()

            response = {"message": "Successfully logged out"}
            return response, 200

        except Exception as e:
            print(e)
            response = {"message": "Some error occurred. Please try again."}
            return response, 500


class DebugAPI(MethodView):
    def get(self):
        try:
            user = User(
                username="apple_test",
                email="test@appl.com",
                password="Caramelo22",
                roles=["member"],
                extra_info={},
                refresh_token=b"",
            )

            db.session.add(user)
            db.session.commit()

            response = {"message": "Successfully created test user"}
            return response, 200

        except Exception as e:
            print(e)
            response = {"message": "Some error occurred. Please try again."}
            return response, 500


registration_view = RegisterAPI.as_view("register_api")
login_view = LoginAPI.as_view("login_api")
logout_view = LogoutAPI.as_view("logout_api")
refresh_view = RefreshAPI.as_view("refresh_api")
debug_view = DebugAPI.as_view("debug_api")

auth_blueprint.add_url_rule(
    "/api/v1/user/auth/register", view_func=registration_view, methods=["POST"]
)

auth_blueprint.add_url_rule(
    "/api/v1/user/auth/login", view_func=login_view, methods=["POST"]
)

auth_blueprint.add_url_rule(
    "/api/v1/user/auth/refresh", view_func=refresh_view, methods=["POST"]
)

auth_blueprint.add_url_rule(
    "/api/v1/user/auth/logout", view_func=logout_view, methods=["GET"]
)

auth_blueprint.add_url_rule(
    "/api/v1/user/auth/debug", view_func=debug_view, methods=["GET"]
)
