from functools import wraps

from flask import request, abort


def json_type_validate(json_schema: dict):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            json: dict = request.json
            if not json:
                abort(400)

            for key, type_ in json_schema.items():
                value = json.get(key)
                if type(value) is not type_:
                    break
            else:
                return fn(*args, **kwargs)
            abort(400)

        return wrapper

    return decorator


SURVEY_POST_JSON = dict(name=str, birthDate=str, gender=int, disturbanceFactor=int, favoriteFood=int)
