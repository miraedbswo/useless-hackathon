def make_parameter(name: str, discription: str, _in='json', param_type='str', required=True):
    return {
        'name': name,
        'description': discription,
        '_in': _in,
        'type': param_type,
        'required': required
    }

