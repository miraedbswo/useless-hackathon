from typing import List

from flask import jsonify
from flasgger import swag_from
from flask_restful import Resource

# from app.decorator import LINK_GET_JSON, json_type_validate
from app.doc.link import LINK_GET
from app.model.survey import SurveyModel
from app.model.link import LinkModel


class Link(Resource):
    @swag_from(LINK_GET)
    def get(self, phone_num: str):
        survey = SurveyModel.get_survey_by_phone_num(phone_num)
        favorite_food = survey.favorite_food
        link: List[str, str] = LinkModel.objects(type=favorite_food).first().link

        return jsonify({
            'imageUrl': link[0],
            'videoUrl': link[1]
        })
