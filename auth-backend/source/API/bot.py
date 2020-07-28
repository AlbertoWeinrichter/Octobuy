from flask import Blueprint, make_response

from source.services.permissions import role_required
from flask.views import MethodView
from source.tasks.android import snkrs

bot_blueprint = Blueprint("bot", __name__)


class BotViewAPI(MethodView):

    # @role_required("member")
    def get(self, product_id):
        print("RUNNING BOT TASK")

        task_id = 1
        result = snkrs.delay(task_id)
        result.wait()

        response = {"task": "Task {task_id} created".format(task_id=task_id)}
        return make_response(response), 200


bot_view = BotViewAPI.as_view("bot_api")
bot_blueprint.add_url_rule(
    "/api/v1/user/bot/<product_id>", view_func=bot_view, methods=["GET"]
)
