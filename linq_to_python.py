def select(collection: list, selector) -> list:
    
    result = list()
    for item in collection:
        result.append(selector(item))
    
    return result

def where(collection: list , condition) -> list:

    result = list()
    for item in collection:
        if condition(item):
            result.append(item)
    
    return result

def count(collection:list, condition) -> list:
    cnt = 0

    for item in collection:
        if condition(item):
            cnt+=1

    return cnt

def to_dict(collection:list, key_selector, value_selector) -> dict:
    result = dict()

    for item in collection:
        key = key_selector(item)
        if not key in result:
            result[key] = value_selector(item)

    return result

def dict_select(dictionary:dict, selector) -> list:
    result = list()
    for key in dictionary:
        result.append(selector(key, dictionary[key]))
    return result

def group_by(collection:list, selector)->dict:
    result = dict()

    for item in collection:
        key = selector(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = list()
            result[key].append(item)
    
    return result
