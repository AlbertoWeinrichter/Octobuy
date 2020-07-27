from flask.views import MethodView
from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import get_jwt_identity

from source.conf.extensions import db
from source.models.publication import Publication, PublicationSchema, PublicationListSchema, PublicationSchema
from source.services.permissions import role_required

publication_blueprint = Blueprint('publication', __name__)


class PublicationEditorAPI(MethodView):

    # Create article #
    @role_required("member")  # TODO: change to editor or admin
    def post(self):
        try:
            post_data = request.get_json()
            identity = get_jwt_identity()

            publication_schema = PublicationSchema(
                author=identity["user_id"],
                type_of=post_data['typeOf'],
                title=post_data['title'],
                slug=post_data['slug'],
                description=post_data['description'],
                published_at=post_data['publicationDate'],
                cover_image=post_data['coverImage'],
                social_image=post_data['socialImage'],
                body_html=post_data['bodyHtml'],
                tags=post_data['tags'],
                summary=post_data['summary']
            )

            publication_object = Publication(**publication_schema.dict())

            db.session.add(publication_object)
            db.session.commit()

            response = {
                'message': 'Publication created'
            }
            return response, 201

        except Exception as e:
            print(e)
            responseObject = {
                'message': 'Some error occurred'
            }
            return make_response(jsonify(responseObject)), 500

    @role_required("member")  # TODO: change to editor or admin
    def get(self):
        try:
            identity = get_jwt_identity()
            publications = Publication.query.filter_by(author=identity["user_id"]).all()

            response = PublicationListSchema(
                publication_list=[PublicationSchema(**p._asdict()) for p in publications]
            ).dict()

            return make_response(response), 200

        except Exception as e:
            responseObject = {
                'message': 'Some error occurred: {error}'.format(error=e)
            }
            return make_response(jsonify(responseObject)), 500

    # def get(self, slug):
    #     try:
    #         publication = Publication.query.filter_by(slug=slug).first()
    #
    #         publication_response = {}
    #         response = {
    #             'status': 'success',
    #             'message': 'Guest content',
    #             'publication': publication_response
    #         }
    #         return make_response(response), 200
    #
    #     except Exception as e:
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'Some error occurred'
    #         }
    #         return make_response(jsonify(responseObject)), 500


publication_view = PublicationEditorAPI.as_view('publication_api')
# publication_blueprint.add_url_rule(
#     '/api/v1/publication/',
#     defaults={'slug': None},
#     view_func=publication_view,
#     methods=['GET'],
# )
#
# publication_blueprint.add_url_rule(
#     '/api/v1/publication/<slug>',
#     view_func=publication_view,
#     methods=['GET'],
# )

publication_blueprint.add_url_rule(
    '/api/v1/publication',
    view_func=publication_view,
    methods=['POST']
)

publication_blueprint.add_url_rule(
    '/api/v1/publication',
    view_func=publication_view,
    methods=['GET']
)
