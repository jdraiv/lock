
import os


def set_keys(*args):
    p_env = os.environ.get('P_ENV', False)
    keys = {}

    if p_env:
        print("Running on production environment")
        for key in args:
            keys[key] = os.environ.get('key', None)
    else:
        print("Running on development environment")
        from secret import keys as private_keys

        for key in args:
            keys[key] = private_keys[key]
    return keys

    