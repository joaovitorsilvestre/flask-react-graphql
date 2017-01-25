from graphql.utils.ast_to_dict import ast_to_dict

def generic_resolver(mongoObject, grapheneObject, args, info):
    fields = [k for k, v in get_fields(info).items() if k[:2] != '__']
    result = mongoObject.objects(**args).only(*fields).first()

    if result:
        a = {f: getattr(result, f) for f in fields}
        return grapheneObject(**a)
    else:
        return None

def generic_resolver_list(mongoObject, grapheneObject, args, info):
    fields = [k for k, v in get_fields(info).items() if k[:2] != '__']
    users = mongoObject.objects(**args).only(*fields)

    if users:
        def get_user_attrs(u):
            return {f: getattr(u, f) for f in fields}

        return [grapheneObject(**get_user_attrs(u)) for u in users]
    else:
        return []

# author: mixxorz
def collect_fields(node, fragments):
    """Recursively collects fields from the AST
    Args:
        node (dict): A node in the AST
        fragments (dict): Fragment definitions
    Returns:
        A dict mapping each field found, along with their sub fields.
        {'name': {},
         'sentimentsPerLanguage': {'id': {},
                                   'name': {},
                                   'totalSentiments': {}},
         'slug': {}}
    """

    field = {}

    if node.get('selection_set'):
        for leaf in node['selection_set']['selections']:
            if leaf['kind'] == 'Field':
                field.update({
                    leaf['name']['value']: collect_fields(leaf, fragments)
                })
            elif leaf['kind'] == 'FragmentSpread':
                field.update(collect_fields(fragments[leaf['name']['value']],
                                            fragments))

    return field

# author: mixxorz
def get_fields(info):
    """A convenience function to call collect_fields with info
    Args:
        info (ResolveInfo)
    Returns:
        dict: Returned from collect_fields
    """

    fragments = {}
    node = ast_to_dict(info.field_asts[0])

    for name, value in info.fragments.items():
        fragments[name] = ast_to_dict(value)

    return collect_fields(node, fragments)