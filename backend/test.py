from mongoengine import *
from six import with_metaclass
from tools import MyMetaClass
import graphene

connect('testing')

class User(Document):
    name = StringField()
    password = StringField()
    active = BooleanField()

class UserSchema(with_metaclass(MyMetaClass, graphene.ObjectType)):
    __MODEL__ = User

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema, name=graphene.String(),
                          password=graphene.String())

    def resolve_user(self, args, context, info):
        user = User.objects(name=args.get('name')).first()
        return UserSchema(name=user.name, password=user.password)


schema = graphene.Schema(query=Query)

result = schema.execute("""query lol {
    user(name: "joao") {
        name
        password
    }
}""")
print(result.data)