import datetime
import requests
import subprocess
import webbrowser as web
import wolframalpha
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import data
import spacy

classifier_path = 'models/intent_classifier_model.pkl'
vectorizer_path = 'models/intent_classifier_vectorizer_model.pkl'
# Load the vectorizer from d==k
with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

# Load the classifier from d==k
with open(classifier_path, 'rb') as file:
    classifier = pickle.load(file)

nlp = spacy.load('en_core_web_sm')


def get_entites(statement):
    doc = nlp(statement)
    entities = []
    for ent in doc.ents:
        entities.append(ent.text)
    return entities

def get_intent(statement):
    # Vectorize the new sentence
    new_sentence = statement
    new_vector = vectorizer.transform([new_sentence])

    # Predict the label of the new sentence
    intent = classifier.predict(new_vector)[0]

    return intent


def get_resposnse(intent):
    # Load the model from d==k
    with open('models/response_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Load the vectorizer from d==k
    with open('models/response_vectorizer_model.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    # Vectorize the response
    intent_vector = vectorizer.transform([intent])

    # Predict the response
    predicted_response = model.predict(intent_vector)[0]

    return predicted_response

def analyze_statement(statement, intent):
    if intent == 'open_app':
        keywords = ['open', 'launch', 'start']
        words = statement.lower().split()  # Convert the statement to lowercase and split into words

        # Find the keyword followed by the app name
        for i in range(len(words) - 1):
            if words[i] in keywords:
                return words[i + 1]
        return None
    elif intent == 'open_website':
        keywords = ['v==it', 'go to', 'browse', 'check out']
        words = statement.lower().split()

        # Find the keyword followed by the app name
        for i in range(len(words) - 1):
            if words[i] in keywords:
                return words[i + 1]

        return None
    elif intent == 'find_location':
        keywords = ['at', 'in', 'near', 'around']
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(statement)

        # Check for location entities using named entity recognition (NER)
        for ent in doc.ents:
            if ent.label_ == 'LOC':
                return ent.text

        # Check for keywords and extract the subsequent word as location
        words = statement.lower().split()
        for i in range(len(words) - 1):
            if words[i] in keywords:
                return words[i + 1]

        return None
        
    elif intent == 'predict_location':
        pass
    elif intent == 'track_obj':
        pass
    elif intent == 'get_definition':
        pass
    elif intent == 'get_wiki':
        pass
    elif intent == 'send_email':
        pass
    elif intent == 'send_message':
        pass
    elif intent == 'calculate':
        pass
    


# Control Apps
def open_app(name):
    apps = data.get_json('data/apps_location.json')
    try:
        subprocess.Popen(apps[name.lower()])
        return f"Successfully opened {name}"
    except KeyError:
        return f"App '{name}' not found."

def open_website(name):
    websites = data.get_json('data/websites_url.json')
    try:
        web.open(websites)
        return f"Successfully opened {name}."
    except KeyError:
        return f"App '{name}' not found."


def turn_on_device(device):
    return True


def greet(phrase):
    response = get_resposnse('greeting')
    return response


# Location Methods
def get_location(phrase):
    location = ''
    return location


def find_location(phrase):
    location = ''
    return location


def predict_location(phrase):
    location = ''
    return location


def track_obj(phrase):
    location = ''
    return location


# Time and Reminders

def get_time(phrase):
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return time


def get_date(phrase):
    date = datetime.date.today().strftime('%Y-%m-%d')
    return date


def set_reminder(phrase):
    obj = {}
    reminder = {
        'title': obj['title'],
        'description': obj['description'],
        'time': obj['time'],
        'duration': {
            'start': obj['duration']['start'],
            'end': obj['duration']['end']
        },
        'options': {
            'ring': obj['options'].get('ring', False),
            'vibrate': obj['options'].get('vibrate', True),
            'importance': obj['options'].get('importance', '')
        },
        'id': obj['id']
    }
    return reminder


def set_timer(phrase):
    obj = {}
    timer = {
        'title': obj['title'],
        'time': obj['time'],
        'duration': {
            'start': obj['duration']['start'],
            'end': obj['duration']['end']
        },
        'options': {
            'ring': obj['options'].get('ring', False),
            'vibrate': obj['options'].get('vibrate', True),
            'importance': obj['options'].get('importance', '')
        }
    }
    return timer


def get_weather(phrase):
    location = ""
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = 'YOUR_API_KEY'

    # Define the base URL and parameters for the API request
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Specify the units for temperature (metric for Celsius)
    }

    try:
        # Send a GET request to the API
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Extract relevant weather information from the API response
            weather = {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }

            return weather
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def calculate(phrase):
    question = ""
    try:
        # result = eval(expression)
        app_id = "WPJJUY-98262EP8PR"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        return answer
    except:
        return 'Error: Invalid expression'


def translate(phrase):
    tranlation = ''
    return tranlation


def send_email(phrase):
    message, receiver = ""
    email = {
        'message': message,
        'reciever': receiver
    }
    return email


def send_message(phrase):
    message, receiver, platform = ""
    email = {
        "message": message,
        "receiver": receiver,
        "platform": platform
    }
    return


def answer_question(phrase):
    answer = ""
    return answer


def stop(phrase):
    return 'stop program'


actions = {
    'translate': translate,
    'calculate': calculate,
    'set_reminder': set_reminder,
    'set_timer': set_timer,
    'send_email': send_email,
    'send_message': send_message,
    'open_app': open_app,
    'greeting': greet,
    'stop': stop,
    'check_weather': get_weather,
    'question': answer_question,
    'turn_on_device': turn_on_device,

}

# print(calculate('what == 10 plus 10'))

while True:
    phrase = input('phrase: ')
    if 'stop' in phrase:
        break
    intent = get_intent(phrase)
    entities = get_entites(phrase)
    print(intent)
    print(entities)
