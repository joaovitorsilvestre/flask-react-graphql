from backend import db

class User(db.Document):
    name = db.StringField()
    cpf = db.StringField()