from app.extension import db


class UserModel(db.Document):
    phone_number = db.StringField(
        primary_key=True
    )

    name = db.StringField(
        max_length=5,
        required=True
    )

    birth_date = db.StringField(
        required=True
    )

    gender = db.IntField(
        max_value=1
    )