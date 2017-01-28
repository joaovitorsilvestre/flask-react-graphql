import graphene
from flask_graphql import GraphQLView

from backend import app
from backend.User.schema import UserSchema, CreateUser, Me
from backend.Product.schema import ProductSchema, CreateProduct

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_product = CreateProduct.Field()

class Querys(graphene.ObjectType):
    me = graphene.Field(Me, **Me.fields_types(), resolver=Me.resolver)

    user = graphene.Field(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver)
    users = graphene.List(UserSchema, **UserSchema.fields_types(), resolver=UserSchema.resolver_list)

    product = graphene.Field(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver)
    products = graphene.List(ProductSchema, **ProductSchema.fields_types(), resolver=ProductSchema.resolver_list)

schema = graphene.Schema(query=Querys, mutation=Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))