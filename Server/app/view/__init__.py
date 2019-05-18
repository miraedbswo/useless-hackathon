from flask import Blueprint
from flask_restful import Api

survey_blueprint = Blueprint('survey', __name__)
api = Api(survey_blueprint)

from app.view.survey import Survey
api.add_resource(Survey, '/survey')

from app.view.link import Link
api.add_resource(Link, '/link/<phone_num>')