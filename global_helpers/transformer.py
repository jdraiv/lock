

from react import jsx


def transform_component(file_path, filename):
    try:
        return jsx.transform(file_path, js_path='/static/bundles/{}'.format(filename))
    except:
        raise Exception("Unable to compile")
