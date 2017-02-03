from mongoengine import *
from six import with_metaclass
from tools import MyMetaClass
from backend.Utils import generic_resolver
import graphene

connect('testing')

class User(Document):
    name = StringField()
    password = StringField()
    active = BooleanField()

class UserSchema(with_metaclass(MyMetaClass, graphene.ObjectType)):
    __MODEL__ = User

    @classmethod
    def resolve_user(cls, root, args, context, info):
        model = cls.__MODEL__
        return generic_resolver(model, UserSchema, args, info)

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema, **UserSchema.fields, resolver=UserSchema.resolve_user)

schema = graphene.Schema(query=Query)

result = schema.execute("""query lol {
    user(name: "joao") {
        name
        password
    }
}""")
print(result.data)