import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import data

def get_intent(statement):
    # Load the vectorizer from disk
    with open('vectorizer_model.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    # Load the classifier from disk
    with open('classifier_model.pkl', 'rb') as file:
        classifier = pickle.load(file)

    # Vectorize the new sentence
    new_sentence = statement
    new_vector = vectorizer.transform([new_sentence])

    # Predict the label of the new sentence
    intent = classifier.predict(new_vector)[0]

    return intent



def open_app(name):
    return 'app started....'


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
    time = ''
    return time

def get_date():
    date = ''
    return date

def set_reminder(obj):
    reminder = data.Reminder
    return reminder

def get_reminder():
    reminder = data.Reminder
    return reminder

def set_timer(obj):
    timer = data.timer
    return timer

def calculate():
    return 'None'





print(get_intent('who is somto?'))



