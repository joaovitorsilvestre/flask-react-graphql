from six import with_metaclass


class Utils:
    @staticmethod
    def make_func(name_field):
        def _function(self, args, context, info):
            return getattr(self, name_field)
        return _function

class MyMetaClass(type):
    def __new__(cls, class_name, parents, attrs):
        avoid = ['__module__', '__main__', '__qualname__']

        final_attrs = {}
        gen_func = {}

        attr_names = {k: v for k, v in attrs.items() if k not in avoid and not callable(v)}
        attr_func = {k: v for k, v in attrs.items() if k not in avoid and callable(v)}

        # generate functions
        for k in attr_names:
            if 'resolve_' + k not in attr_func:
                gen_func['resolve_' + k] = Utils.make_func(k)

        final_attrs.update(attr_names)
        final_attrs.update(attr_func)
        final_attrs.update(gen_func)

        print(final_attrs)

        # return type.__new__(cls, class_name, parents, final_attrs)
        return type(class_name, (object,), final_attrs)

class MyClass(with_metaclass(MyMetaClass, object)):
    name = "joao"
    password = "123456"

    def resolve_name(self, args, context, info):
        return self.name

myobject = MyClass()
print(myobject.name)
print(myobject.resolve_name(1,2,3))
print(myobject.resolve_password(1,2,3))