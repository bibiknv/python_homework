import json

def is_correct_json(string):
    try:
        data = json.loads(string)
        data_json = json.dumps(data)
        return True
    except ValueError:
        return False
is_correct_json('number = 17')
