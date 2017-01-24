import graphene

from backend.User.schema import UserSchema
from backend.Product.schema import ProductSchema

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver)

    users = graphene.List(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver_list)

    product = graphene.Field(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver)
    products = graphene.List(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver_list)

schema = graphene.Schema(query=Query)

query = '''
    query something{
        user(name: "joao") {
            name
            password
        }
        products(price: 5.99) {
            name
            price
        }
    }
'''

import json
result = schema.execute(query).data
parsed = json.dumps(dict(result), indent=2, sort_keys=True)

print(parsed)