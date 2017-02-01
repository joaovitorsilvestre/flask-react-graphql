import graphene, re
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    name = db.StringField()
    password = db.StringField()


#############
def resolve_name(self, args, context, info):
    return self.name or 'joao'

SubClass = type('UserSchema', (graphene.ObjectType,), dict(name=graphene.String(), password=graphene.String(), resolve_name=resolve_name))




class Query(graphene.ObjectType):
    user = graphene.Field(SubClass, name=graphene.String(),
                               password=graphene.String())

    def resolve_user(self, args, context, info):
        return SubClass(**args)

schema = graphene.Schema(query=Query)
result = schema.execute("""{
    user(name: "joao") {
        name
    }
}
""")
print(result.data)