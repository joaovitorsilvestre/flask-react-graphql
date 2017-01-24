import graphene

from backend.User.models import User
from backend.Utils import generic_resolver, generic_resolver_list


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