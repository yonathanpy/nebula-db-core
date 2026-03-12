import json


def serialize(obj):

    return json.dumps(obj)


def deserialize(data):

    return json.loads(data)
