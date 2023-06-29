import json

def get_data():
    # Load the JSON data
    with open('data/intent_data.json', 'r') as file:
        data = json.load(file)

    intents = []
    statements = []
    responses = []

    for item in data:
        intent = item['intent']
        statement = item['statement']

        if item.get('responses') is not None:
            for response in item.get('responses'):
                intents.append(intent)
                statements.append(statement)
                responses.append(response)
        else:
            response = item['response']

            intents.append(intent)
            statements.append(statement)
            responses.append(response)

    new_data = []
    for i in range(len(intents)):
        obj = {
            "intent": intents[i],
            "statement": statements[i],
            "response": responses[i]
        }
        new_data.append(obj)
    else:
        print('done reorganizing dataset')
    return new_data, intents, statements, responses

