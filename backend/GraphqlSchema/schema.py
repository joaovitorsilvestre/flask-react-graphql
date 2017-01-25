import graphene
from flask_graphql import GraphQLView

from backend import app
from backend.User.schema import UserSchema
from backend.Product.schema import ProductSchema

class Query(graphene.ObjectType):
    user = graphene.Field(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver)
    users = graphene.List(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver_list)

    product = graphene.Field(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver)
    products = graphene.List(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver_list)

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
# app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema))