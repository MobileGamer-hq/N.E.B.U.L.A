import json
def getIntentData():
    with open('intent_data.json') as json_data:
        intents = json.load(json_data)
        print(intents)
        
    sentences = []
    labels = []
    for intent in intents:
        print(intent)
        print(intent.get('intent'))

getIntentData()