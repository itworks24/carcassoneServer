# замените user, password, ds049945.mongolab.com, example на ваши данные доступа к БД.
# MONGO_URI = "mongodb://root:0WYyTixLojXX>@ds141068.mlab.com:41068/carcassone"
MONGO_HOST = "ds141068.mlab.com"
MONGO_PORT = 41068
MONGO_USERNAME = "root"
MONGO_PASSWORD = "0WYyTixLojXX"
MONGO_DBNAME = "carcassone"
#MONGO_AUTH_MECHANISM = "MONGODB-CR"
MONGO_AUTH_MECHANISM = "SCRAM-SHA-1"

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'tileTypes': {
        'schema': {
            'imgUrl': {'type': 'string', 'required': True},
            'top': {
                'type': 'dict',
                'schema': {
                    'contentType': {'type': 'string'},
                    'to': {'type': 'list'}
                }
            },
            'bottom': {
                'type': 'dict',
                'schema': {
                    'contentType': {'type': 'string'},
                    'to': {'type': 'list'}
                }
            },
            'left': {
                'type': 'dict',
                'schema': {
                    'contentType': {'type': 'string'},
                    'to': {'type': 'list'}
                }
            },
            'right': {
                'type': 'dict',
                'schema': {
                    'contentType': {'type': 'string'},
                    'to': {'type': 'list'}
                }
            },
        }
    },

    'gameTiles': {
        'schema': {
            'ident': {
                'type': 'dict',
                'unique': True,
                'required': True,
                'schema':{
                    'x': {'type': 'integer', 'required': True},
                    'y': {'type': 'integer', 'required': True},
                    'game': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'games',
                    'field': '_id',
                    'embeddable': True
                }
            },
                }
            },
            'rotation': {'type': 'integer', 'required': True, 'default': 0},
            'tileType': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'tileTypes',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'author': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'gamers',
                    'field': '_id',
                    'embeddable': True
                }
            }
        }
    },

    'meeples': {
        'schema': {
            'meepleType': {'type': 'string', 'allowed': ['regular', 'large']},
            'position': {'type': 'integer', 'allowed': [1, 2, 3, 4, 5]},
            'gameTile': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'gameTiles',
                    'field': '_id',
                    'embeddable': True
                },
            },
            'owner': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'gamers',
                    'field': '_id',
                    'embeddable': True
                },
            },
        }
    },

    'gamers': {
        'schema': {
            'meepleCount': {'type': 'integer'},
            'game': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'games',
                    'field': '_id',
                    'embeddable': True
                },
            },
            'user': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'users',
                    'field': '_id',
                    'embeddable': True
                },
            },
        }
    },

    'games': {
        'schema': {
            'name' : {'type': 'string' },
            'startDate': {'type': 'datetime', 'required': True},
        }
    },

    'users': {
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': True,
            },
            'role': {
                'type': 'list',
                'allowed': ["admin", "gamer"],
            },
        }
    },
}
