import datetime
import requests
import subprocess
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import data

def get_intent(statement):
    # Load the vectorizer from disk
    with open('models/intent_classifier_vectorizer_model.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    # Load the classifier from disk
    with open('models/intent_classifier_model.pkl', 'rb') as file:
        classifier = pickle.load(file)

    # Vectorize the new sentence
    new_sentence = statement
    new_vector = vectorizer.transform([new_sentence])

    # Predict the label of the new sentence
    intent = classifier.predict(new_vector)[0]

    return intent

def get_resposnse(intent):
    # Load the model from disk
    with open('models/response_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Load the vectorizer from disk
    with open('models/response_vectorizer_model.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    # Vectorize the response
    intent_vector = vectorizer.transform([intent])

    # Predict the response
    predicted_response = model.predict(intent_vector)[0]

    return predicted_response

#Control Apps
def open_app(name):
    apps = data.get_json('data/apps_location.json')
    try:
        subprocess.Popen(apps[name.lower()])
        return f"Successfully opened {name} app."
    except KeyError:
        return f"App '{name}' not found."


#Location Methods
def get_location():
    location = ''
    return location

def find_location(place):
    location = ''
    return location

def predict_location(points):
    location = ''
    return location

def track_obj(obj):
    location = ''
    return location

#Time and Reminders

def get_time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return time

def get_date():
    date = datetime.date.today().strftime('%Y-%m-%d')
    return date

def set_reminder(obj):
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

def set_timer(obj):
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

def get_weather(location):
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


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return 'Error: Invalid expression'
    



