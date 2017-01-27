from backend.User.models import User
from backend.Product.models import Product
from backend import db


class Cart(db.Document):
    user = db.ReferenceField(User)
    products = db.ListField(db.ReferenceField(Product))