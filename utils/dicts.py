def get_val(collection: dict, input_key, default='git'):
    if len(collection) != 0 and type(collection) == dict:
        for key, value in collection.items():
            if key == input_key:
                return value
    return default



