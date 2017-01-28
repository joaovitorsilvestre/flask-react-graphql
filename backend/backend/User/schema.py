import graphene

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
        from flask_login import current_user
        return Me(name=current_user.name) if current_user.is_active else None

    @staticmethod
    def fields_types():
        return {
            'name': graphene.String(),
        }