import os


class Config:
    SERVICE_NAME = 'gura'

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB', 'gura'),
        'host': os.getenv('MONGO_HOST', 'ds237955.mlab.com'),
        'port': os.getenv('MONGO_PORT', 37955),
        'username': os.getenv('MONGO_ID', 'wisemuji'),
        'password': os.getenv('MONGO_PW', 'spoqa6')
    }

    SWAGGER = {
        'title': 'Spoqa Hackathon',
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        'uiversion': 3,
        'specs_route': '/docs',

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0'
        },

        'host': 'localhost',
        'basePath': '/api'
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Survey',
                'description': '설문조사 관련 API'
            }
        ]
    }


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}