import os

import config

APP_ROOT_DIR = os.path.pardir(config.__file__)

DEFAULT_METHODS_PARAMS_LOCATION = {
    'post': 'json',
    'patch': 'json',
    'put': 'json',
    'get': 'args',
    'delete': 'args',
}

