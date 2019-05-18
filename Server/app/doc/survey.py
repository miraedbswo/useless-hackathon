from app.doc import make_parameter


SURVEY_POST = {
    'tags': ['Survey'],
    'description': '설문조사 작성',
    'parameters': [
        make_parameter('name', '사용자 이름'),
        make_parameter('birthDate', '사용자 생년월일'),
        make_parameter('gender', '사용자 성별'),
        make_parameter('disturbanceFactor', '다이어트에 방해가 되는 요소 (0~4)', param_type='int'),
        make_parameter('favoriteFood', '가장 좋아하는 음식 (0~5)', param_type='int'),
    ],
    'responses': {
        '200': {
            'description': '설문조사 작성 성공'
        },
        '400': {
            'description': '설문조사 작성 실패(incorrect formatting)'
        }
    }
}
