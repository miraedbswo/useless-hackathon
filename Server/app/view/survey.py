from flasgger import swag_from
from flask_restful import Resource

from app.doc import SURVEY_POST


class Survey(Resource):
    @swag_from(SURVEY_POST)
    def post(self):
        pass
