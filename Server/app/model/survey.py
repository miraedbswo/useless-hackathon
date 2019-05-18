from app.extension import db


class SurveyModel(db.Document):
    """
    설문 조사 리스트가 나오면, 그에 맞게 모델 작성.
    int 기반으로 하여 그 기준에 맞는 url을 전송하기 위함.
    ex) 11시에 야식이 땡긴다 -> 그 case에 맞게 보내줌
    """
    pass
