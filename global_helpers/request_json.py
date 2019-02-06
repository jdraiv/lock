

def request_json(request_obj, json_args):
    data = {}
    call_status = True

    for json_val in json_args:
        try:
            data[json_val] = request_obj.json[json_val]
        except:
            data[json_val] = 'None'
            valid_call =  False

    return {'data': data, 'valid_call': call_status}
