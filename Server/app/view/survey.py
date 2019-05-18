from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource

from app.decorator import SURVEY_POST_JSON, json_type_validate
from app.doc.survey import SURVEY_POST
from app.model.survey import SurveyModel
from app.model.user import UserModel


class Survey(Resource):
    @json_type_validate(SURVEY_POST_JSON)
    @swag_from(SURVEY_POST)
    def post(self):
        name = request.json['name']
        birth_date = request.json['birthDate']
        gender = request.json['gender']
        phone_number = request.json['phoneNumber']
        disturbance_factor = request.json['disturbanceFactor']
        favorite_food = request.json['favoriteFood']

        user = UserModel(
            name=name,
            birth_date=birth_date,
            gender=gender,
            phone_number=phone_number
        )
        user.save()

        SurveyModel(
            disturbance_factor=disturbance_factor,
            favorite_food=favorite_food,
            user=user
        ).save()

        return Response('', 200)
