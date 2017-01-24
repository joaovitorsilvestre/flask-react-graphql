import graphene

from backend.User.models import User
from backend.Utils import get_fields


class UserSchema(graphene.ObjectType):
    name = graphene.String()
    password = graphene.String()

    def resolve_name(self, args, context, info):
        return self.name
    def resolve_password(self, args, context, info):
        return self.password

    @staticmethod
    def resolver(root, args, context, info):
        fields = [k for k, v in get_fields(info).items()]
        user = User.objects(**args).only(*fields).first()

        if user:
            a = {f: getattr(user, f) for f in fields}
            return UserSchema(**a)
        else:
            return None

    @staticmethod
    def resolver_list(root, args, context, info):
        fields = [k for k, v in get_fields(info).items()]
        users = User.objects(**args).only(*fields)

        if users:
            def get_user_attrs(u): return {f: getattr(u, f) for f in fields}
            return [UserSchema(**get_user_attrs(u)) for u in users]
        else:
            return []

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema,
                          name=graphene.String(),
                          password=graphene.String(),
                          resolver=UserSchema.resolver)

    users = graphene.List(UserSchema,
                          name=graphene.String(),
                          password=graphene.String(),
                          resolver=UserSchema.resolver_list)

schema = graphene.Schema(query=Query)

query = '''
    query something{
        users(name: "joao", password:"123456") {
            name
            password
        }
    }
'''

import json
result = schema.execute(query).data
parsed = json.dumps(dict(result), indent=2, sort_keys=True)

print(parsed)