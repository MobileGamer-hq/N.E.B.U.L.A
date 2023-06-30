import datetime
import requests
import subprocess
import webbrowser as web
import wolframalpha
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import data
import spacy

class Actions:
    def __init__(self):
        self.classifier_path = 'models/intent_classifier_model.pkl'
        self.vectorizer_path = 'models/intent_classifier_vectorizer_model.pkl'
        self.nlp = spacy.load('en_core_web_sm')
        self.vectorizer = self.load_model(self.vectorizer_path)
        self.classifier = self.load_model(self.classifier_path)

    def load_model(self, model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def get_entities(self, statement):
        doc = self.nlp(statement)
        entities = []
        for ent in doc.ents:
            entities.append(ent.text)
        return entities

    def get_intent(self, statement):
        new_sentence = statement
        new_vector = self.vectorizer.transform([new_sentence])
        intent = self.classifier.predict(new_vector)[0]
        return intent

    def get_response(self, intent):
        response_model_path = 'models/response_model.pkl'
        response_vectorizer_path = 'models/response_vectorizer_model.pkl'
        response_model = self.load_model(response_model_path)
        response_vectorizer = self.load_model(response_vectorizer_path)
        intent_vector = response_vectorizer.transform([intent])
        predicted_response = response_model.predict(intent_vector)[0]
        return predicted_response

    def analyze_statement(self, statement, intent):
        if intent == 'open_app':
            def open_app_analyzer():
                keywords = ['open', 'launch', 'start']
                words = statement.lower().split()
                for i in range(len(words) - 1):
                    if words[i] in keywords:
                        return words[i + 1]
                return None

            entities = open_app_analyzer()

        elif intent == 'open_website':
            keywords = ['visit', 'go to', 'browse', 'check out']
            words = statement.lower().split()
            for i in range(len(words) - 1):
                if words[i] in keywords:
                    return words[i + 1]
            return None

        elif intent == 'find_location':
            keywords = ['at', 'in', 'near', 'around']
            doc = self.nlp(statement)
            for ent in doc.ents:
                if ent.label_ == 'LOC':
                    return ent.text
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
    def open_app(self, name):
        apps = data.get_json('data/apps_location.json')
        try:
            subprocess.Popen(apps[name.lower()])
            return f"Successfully opened {name}"
        except KeyError:
            return f"App '{name}' not found."

    def open_website(self, name):
        websites = data.get_json('data/websites_url.json')
        try:
            web.open(websites)
            return f"Successfully opened {name}."
        except KeyError:
            return f"App '{name}' not found."

    def turn_on_device(self, device):
        return True

    def greet(self, phrase):
        response = self.get_response('greeting')
        return response

    # Location Methods
    def get_location(self, phrase):
        location = ''
        return location

    def find_location(self, phrase):
        location = ''
        return location

    def predict_location(self, phrase):
        location = ''
        return location

    def track_obj(self, phrase):
        location = ''
        return location

    # Time and Reminders

    def get_time(self, phrase):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        return time

    def get_date(self, phrase):
        date = datetime.date.today().strftime('%Y-%m-%d')
        return date

    def set_reminder(self, phrase):
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

    def set_timer(self, phrase):
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

    def get_weather(self, phrase):
        location = ""
        api_key = 'YOUR_API_KEY'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
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

    def calculate(self, phrase):
        question = ""
        try:
            app_id = "WPJJUY-98262EP8PR"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            return answer
        except:
            return 'Error: Invalid expression'

    def translate(self, phrase):
        translation = ''
        return translation

    def send_email(self, phrase):
        message, receiver = ""
        email = {
            'message': message,
            'receiver': receiver
        }
        return email

    def send_message(self, phrase):
        message, receiver, platform = ""
        email = {
            "message": message,
            "receiver": receiver,
            "platform": platform
        }
        return

    def answer_question(self, phrase):
        answer = ""
        return answer

    def stop(self, phrase):
        return 'stop program'

if __name__ == '__main__':
    actions = Actions()
    while True:
        phrase = input('phrase: ')
        if 'stop' in phrase:
            break
        intent = actions.get_intent(phrase)
        entities = actions.get_entities(phrase)
        print(intent)
        print(entities)
