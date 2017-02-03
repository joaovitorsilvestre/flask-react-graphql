from mongoengine import *
import graphene


class Utils:
    @staticmethod
    def make_func(name_field):
        def _function(self, args, context, info):
            return getattr(self, name_field)
        return _function


class MyMetaClass(type):
    def __new__(cls, class_name, parents, attrs):
        #create auto result
        model = attrs.get('__MODEL__')

        model_attrs = {k: v for k, v in model._fields.items() if k != 'id'}

        a = {
            StringField: graphene.String(),
            BooleanField: graphene.Boolean()
        }

        for k, v in model_attrs.items():
            attrs[k] = a.get(type(v))

        return type(class_name, (graphene.ObjectType,), attrs)
