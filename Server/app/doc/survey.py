from app.doc import make_parameter


SURVEY_POST = {
    'tags': ['Survey'],
    'description': '설문조사 작성',
    'parameters': [
        make_parameter('test', 'test'),
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
