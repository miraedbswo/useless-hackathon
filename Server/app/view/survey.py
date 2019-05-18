from flasgger import swag_from
from flask_restful import Resource

from app.decorator import SURVEY_POST_JSON, json_type_validate
from app.doc.survey import SURVEY_POST


class Survey(Resource):
    @json_type_validate(SURVEY_POST_JSON)
    @swag_from(SURVEY_POST)
    def post(self):
        pass
