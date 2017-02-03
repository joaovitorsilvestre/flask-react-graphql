from mongoengine import *
import graphene
from backend.Utils import generic_resolver


class Utils:
    @staticmethod
    def make_func(name_field):
        def _function(self, args, context, info):
            return getattr(self, name_field)
        return _function

class MyMetaClass(type):
    def __new__(cls, class_name, parents, attrs):
        model = attrs.get('__MODEL__')
        model_attrs = {k: v for k, v in model._fields.items() if k != 'id'}

        dict_convert = {
            StringField: graphene.String(),
            BooleanField: graphene.Boolean()
        }

        ## attr to store the type for use it in graphene.Field(... username=graphene.String etc
        attrs['fields'] = {}

        for k, v in model_attrs.items():
            respective_graphene = dict_convert.get(type(v))

            attrs[k] = respective_graphene
            attrs['fields'][k] = respective_graphene

        return type(class_name, (graphene.ObjectType,), attrs)
