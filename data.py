import json
#data manager functions
def save_json(obj):

    return obj

def get_json(data_type):
    
    
    return data_type

#data models
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
  "freinds": [],
  "enemies": [],
  "relationship": '',
  "details": {
      
  }
}

Place = {
  'name': '',
  'address': '',
  'about': '',
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
}