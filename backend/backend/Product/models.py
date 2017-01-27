from backend import db

class Product(db.Document):
    name = db.StringField()
    price = db.FloatField()