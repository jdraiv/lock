

def internal_response(status, message='None', data=None):
    if data != None:
        return {'status': status, 'message': message, 'data': data}
    return {'status': status, 'message': message}