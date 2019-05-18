from flask import Blueprint
from flask_restful import Api

survey_blueprint = Blueprint('survey', __name__)
api = Api(survey_blueprint)

from .survey import Survey
api.add_resource(Survey)