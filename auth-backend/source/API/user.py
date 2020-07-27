from flask import Blueprint, make_response
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from source.models.user import User, UserSchema
from source.services.permissions import role_required

user_blueprint = Blueprint("user", __name__)


class UserViewAPI(MethodView):
    @role_required("member")
    def get(self, user_id):
        if user_id == "me":
            identity = get_jwt_identity()
            user = User.query.filter_by(id=identity["user_id"]).first()
        else:
            user = User.query.filter_by(id=user_id).first()

        user_response = UserSchema(
            id=user.id,
            username=user.username,
            email=user.email,
            refresh_token=user.refresh_token,
            roles=user.roles,
            extra_info=str(user.extra_info),
        )
        response = {"message": "Successfully logged in", "user": user_response.dict()}
        return make_response(response), 200


user_view = UserViewAPI.as_view("user_api")
user_blueprint.add_url_rule(
    "/api/v1/user/<user_id>", view_func=user_view, methods=["GET"]
)
