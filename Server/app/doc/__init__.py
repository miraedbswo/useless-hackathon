def make_parameter(name: str, discription: str, param_type='str', required=True):
    return {
        'name': name,
        'description': discription,
        'in': 'json',
        'type': param_type,
        'required': required
    }

