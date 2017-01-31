from flask_login import current_user
import graphene

from backend import redis_store

from backend.User.models import User
from backend.Utils import generic_resolver, generic_resolver_list, generic_object_creator


class CreateUser(graphene.Mutation):
    class Input:
        name = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: UserSchema)
    ok = graphene.Boolean()

    def mutate(self, args, context, info):
        user = generic_object_creator(User, args)
        return CreateUser(user=user, ok=user is not None)

class UserSchema(graphene.ObjectType):
    name = graphene.String()
    password = graphene.String()

    def resolve_name(self, args, context, info):
        return self.name
    def resolve_password(self, args, context, info):
        return self.password

    @staticmethod
    def resolver(root, args, context, info):
        return generic_resolver(User, UserSchema, args, info)

    @staticmethod
    def resolver_list(root, args, context, info):
        return generic_resolver_list(User, UserSchema, args, info)

    @staticmethod
    def fields_types():
        return {
            'name': graphene.String(),
            'passoword': graphene.String()
        }


class Me(graphene.ObjectType):
    name = graphene.String()

    @staticmethod
    def resolver(root, args, context, info):
        auth = context.headers['Authorization']

        if len(auth) == 100:
            user_id = redis_store.get(auth).decode("utf-8")
            user = User.objects(id=user_id).only(**args).first()
            return Me(name=user.name)

        return None

    @staticmethod
    def fields_types():
        return {
            'name': graphene.String(),
        }