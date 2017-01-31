from backend import db


class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    active = db.BooleanField()