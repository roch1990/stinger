schema = {
    'type': 'object',
    'properties': {
        'uri': {
            'type': 'string',
            'format': 'uri',
        },
        'port': {
            'type': 'integer',
            'minimum': 0,
            'maximum': 65535,
        },
        'name': {
            'type': 'string',
            'minLength': 2,
            'maxLength': 100,
        },
        'route': {
            'type': 'string',
            'pattern': '^\/[a-zA-Zа-яА-Я0-9 _\-\/\.]{1,}$',
        },
        'method': {
            'type': 'string',
            'pattern': '^(GET|POST|PATCH|PUT|DELETE)$',
        },
        'timeout': {
            'type': 'integer',
            'minimum': 2,
            'maximum': 600,
        },
        'headers': {
            'type': 'object',
        },
        'payload': {
            'type': 'object',
        },
    },
    'required': [
        'uri',
        'port',
        'name',
        'route',
        'method',
        'timeout',
    ],
}
