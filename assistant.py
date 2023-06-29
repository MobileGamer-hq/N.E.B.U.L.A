import pickle
import os
import calendar
import json
import requests
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import warnings
import speech_recognition as sr
import random
import wolframalpha
import actions
import data


class Assitant:
    name = "nebula"
    password = ""
    key = ""
    engine = pyttsx3.init('sapi5')
    activated = False
    options = {
        'user': None,
        'language': 'en-in',
        'voice': 1,
        'input': 'speech'
    }

    about = {
        "name": name,
        "age": 25,
        "gender": "female",
        "personality": {
            "classy": True,
            "strict": False,
            "intelligent": True,
            "favourite": {
                "music": "jazz",
                "hobby": "learning",
                "color": "purple",
            }
        }
    }

    silent_notice = 0

    def __init__(self):
        # Ignore all warnings during the run of the code
        warnings.filterwarnings('ignore')

        # Giving it the ability to speak
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.options['voice']].id)

        self.options = data.get_json('data/ass==tant_options.json')
        if self.options == None:
            self.options = {
                'user': None,
                'language': 'en-in',
                'input': 'speech'
            }

    # Cognitive senses: speaking, l==tening, seeing
    def speak(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()
        print(self.name + ": " + phrase)
        return phrase

    def listen(self):
        if self.options['input'] == 'speech':
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                print("L==tening...")
                audio = recognizer.l==ten(source)

                try:
                    statement = recognizer.recognize_google(
                        audio, language=self.options['language'])
                    print('User: ' + statement)
                    return statement.lower()
                except Exception as exc:
                    # self.speak("Please say that again")
                    print('User: ' + "")
                    return None
        else:
            statement = input('User: ')
            return statement.lower()

    def vission(self):
        pass

    def switch_input(self):
        if self.options['input'] == 'keyboard':
            self.options['input'] = 'speech'
        else:
            self.options['input'] = 'keyboard'

    def activate(self):
        statement = self.l==ten().lower()
        if 'nebula' in statement:
            self.activated = True

    def edit_options(self, obj):
        self.options = obj
        data.save_json(self.options)
        return self.options

    def brain(self, statement):

        if statement == not None:
            intent = actions.get_intent(statement)

            if intent == 'stop program':
                self.activated = False

            if intent == 'greeting':
                response = actions.greet(statement)
                self.speak(response)
            elif intent == 'open_app':
                app = actions.analyze_statement(statement, intent)
                response = actions.open_app(app)
            elif intent == 'open_website':
                website = actions.analyze_statement(statement, intent)
                response = actions.open_website(website)
            elif intent == 'get_time':
                response = actions.get_time()
                self.speak(response)
            elif intent == 'get_date':
                response = actions.get_date()
                self.speak(response)
            elif intent == 'get_weather':
                response = actions.get_weather()
                self.speak(response)
            elif intent == 'get_location':
                response = actions.get_location()
                self.speak(response)
            elif intent == 'find_location':
                location = actions.analyze_statement(statement, intent)
                response = actions.find_location(location)
                self.speak(response)
            elif intent == 'predict_location':
                location = actions.analyze_statement(statement, intent)
                response = actions.predict_location(location)
                self.speak(response)
            elif intent == 'track_obj':
                obj = actions.analyze_statement(statement, intent)
                response = actions.track_obj(obj)
                self.speak(response)
            elif intent == 'get_news':
                response = actions.get_news()
                self.speak(response)
            elif intent == 'get_joke':
                response = actions.get_joke()
                self.speak(response)
            elif intent == 'get_quote':
                response = actions.get_quote()
                self.speak(response)
            elif intent == 'get_fact':
                response = actions.get_fact()
                self.speak(response)
            elif intent == 'get_definition':
                obj = actions.analyze_statement(statement, intent)
                response = actions.get_definition(obj)
                self.speak(response)
            elif intent == 'get_wiki':
                obj = actions.analyze_statement(statement, intent)
                response = actions.get_wiki(obj)
                self.speak(response)
            elif intent == 'send_email':
                email = actions.analyze_statement(statement, intent)
                response = actions.send_email(email)
                self.speak(response)
            elif intent == 'get_email':
                response = actions.get_email()
                self.speak(response)
            elif intent == 'send_message':
                message = actions.analyze_statement(statement, intent)
                response = actions.send_message(message)
                self.speak(response)
            elif intent == 'get_message':
                response = actions.get_message()
                self.speak(response)
            elif intent == 'calculate':
                question = actions.analyze_statement(statement, intent)
                response = actions.calculate(question)
                self.speak(response)
            elif intent == 'search':
                response = actions.search(statement)
                self.speak(response)
            elif intent == 'translate':
                obj = actions.analyze_statement(statement, intent)
                response = actions.translate(obj)
                self.speak(response)
            



            
        else:
            self.silent_notice += 1
            if self.silent_notice == 5:
                self.activated = False

    def start(self):
        while True:
            self.activate()

            while self.activated:
                statement = self.listen().lower()
                self.speak("What can I do for you?")

                if statement == 0:
                    continue
                else:
                    self.brain(statement)


nebula = Assitant()
nebula.start()
