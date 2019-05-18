from flask import abort

from app.extension import db
from app.model.user import UserModel


class SurveyModel(db.Document):
    """
    설문 조사 리스트가 나오면, 그에 맞게 모델 작성.
    int 기반으로 하여 그 기준에 맞는 url을 전송하기 위함.
    ex) 11시에 야식이 땡긴다 -> 그 case에 맞게 보내줌
    """
    disturbance_factor = db.IntField(
        max_value=4
    )

    favorite_food = db.IntField(
        max_value=5
    )

    user = db.ReferenceField(
        document_type=UserModel
    )

    @classmethod
    def get_survey_by_phone_num(cls, phone_number: str):
        survey = SurveyModel.objects(user=UserModel.objects(phone_number=phone_number).first()).first()
        if not survey:
            abort(403)
        return survey
