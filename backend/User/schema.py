import graphene

from backend.User.models import User


class UserSchema(graphene.ObjectType):
    name = graphene.String()
    passsword = graphene.String()

    def resolve_name(self, args, context, info):
        return self.name
    def resolve_password(self, args, context, info):
        return self.passsword

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema,
                          name= graphene.String(),
                          password=graphene.String())

    def resolve_user(self, args, context, info):
        fields = [k for k, v in args.items()]
        user = User.objects(**args).only(*fields).first()

        if user:
            a = {key: getattr(user, key) for key, val in args.items()}
            return UserSchema(**a)
        else:
            return None

schema = graphene.Schema(query=Query)

query = '''
    query something{
        user(name: "joao") {
            name
        }
    }
'''

import json
result = schema.execute(query).data
parsed = json.dumps(dict(result), indent=2, sort_keys=True)

print(parsed)