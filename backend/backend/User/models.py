from backend import db


class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    active = db.BooleanField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)