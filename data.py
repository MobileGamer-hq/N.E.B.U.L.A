import json
import os


# data manager functions
def clean_json(location):
    with open(location, 'r') as file:
        data = json.load(file)
    # Remove duplicate entries
    unique_data = [dict(t) for t in {tuple(d) for d in data}]

    # Convert the list of dictionaries back to JSON
    cleaned_data = json.dumps(unique_data, indent=2)

    print(cleaned_data)
    with open(location, 'w') as file:
        json.dump(clean_json, file, indent=4)
    return cleaned_data


def save_json(obj, location):
    with open(location, 'w') as file:
        json.dump(obj, file, indent=4)

    return obj


def get_json(location):
    if os.path.exists(location):
        with open(location, 'r') as file:
            obj = json.load(file)
        return obj
    else:
        return None


def append_json(obj, location):
    if os.path.exists(location):
        with open(location, 'r') as file:
            data = json.load(file)
        data.append(obj)
        with open(location, 'w') as file:
            json.dump(data, file, indent=4)
        return data
    else:
        return None


def pop_json(obj, location):
    if os.path.exists(location):
        with open(location, 'r') as file:
            data = json.load(file)
        data.pop(obj)
        with open(location, 'w') as file:
            json.dump(data, file, indent=4)
        return data

def manage_assistant_data():
    data_path = 'data/users_data'
    data = Assistant_Data
    data["about"] = get_json(data_path+"about")
    data["user"] = get_json(data_path+"user")


# data models
Assistant_Data = {
    "about": None,
    "user": None,
    "users_with_access": [],
    "users_data": {
        "timers": [],
        "reminders": [],
        "alarms": [],
        "projects": [],
        "apps": [],

    },
    "options": None
}
Person = {
    "name": {
        "nick_name": "",
        "first": "",
        "last": "",
        "other": []
    },
    "date_of_birth": {
        "day": "",
        "month": "",
        "year": ""
    },
    "age": 0,
    "occupation": "",
    "address": {
        "home": "",
        "office": "",
        "others": []
    },
    "friends": [],
    "enemies": [],
    "details": None,
    "id": ""
}

Friend = {
    "relationship": "friend",
    "friends": [],
}

Place = {
    'name': '',
    'address': '',
    'about': '',
    'id': ''
}

Reminder = {
    'title': '',
    'description': '',
    'time': '',
    'duration': {
        'start': '',
        'end': ''
    },
    'options': {
        'ring': False,
        'vibrate': True,
        'importance': ''
    },
    'id': ''
}

timer = {
    'title': '',
    'time': '',
    'duration': {
        'start': '',
        'end': ''
    },
    'options': {
        'ring': False,
        'vibrate': True,
        'importance': ''
    },
    'id': ''
}
