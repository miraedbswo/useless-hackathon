from app.doc import make_parameter


LINK_GET = {
    'tags': ['Link'],
    'description': '잠금화면에 띄워줄 영상 or 이미지 url 제공',
    'parameters': [
        make_parameter('phone_num', '핸드폰 번호', _in='url'),
    ],
    'responses': {
        '200': {
            'description': '요청 성공',
            'examples': {
                '': {
                    "imageUrl": "https://s3.ap-northeast-2.amazonaws.com/useless-project/0/1.mp4",
                    "videoUrl": "https://baemin.me/IHJ2g5YDW"
                }
            }
        },
        '403': {
            'description': '회원가입 되지 않은 전화번호'
        }
    }
}
