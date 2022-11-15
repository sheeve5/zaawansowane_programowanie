import json


def serialize(my_list: list):
    strings: list[str] = []
    for item in my_list:
        strings.append(item.__dict__)
    return json.JSONEncoder().encode(strings)


def get_int(string: str) -> int:
    if string.isdigit():
        return int(string)
    else:
        return -1

