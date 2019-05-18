from app.extension import db


class LinkModel(db.Document):
    type = db.IntField()

    link = db.ListField(
        db.StringField()
    )

