import graphene

from backend.Product.models import Product
from backend.Utils import get_fields, generic_resolver, generic_resolver_list

class ProductSchema(graphene.ObjectType):
    name = graphene.String()
    price = graphene.Float()

    def resolve_name(self, args, context, info):
        return self.name
    def resolve_price(self, args, context, info):
        return self.price

    @staticmethod
    def resolver(root, args, context, info):
        return generic_resolver(Product, ProductSchema, args, info)

    def resolver_list(self, args, context, info):
        return generic_resolver_list(Product, ProductSchema, args, info)

    @staticmethod
    def fields_types():
        return {
            'name': graphene.String(),
            'price': graphene.Float()
        }