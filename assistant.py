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
import pickle

from actions import Actions


class Assistant:
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

        self.options = self.load_options()
        if self.options is None:
            self.options = {
                'user': None,
                'language': 'en-in',
                'input': 'speech'
            }

    def load_options(self):
        try:
            with open('assistant_options.pickle', 'rb') as f:
                options = pickle.load(f)
                return options
        except FileNotFoundError:
            return None

    def save_options(self):
        with open('assistant_options.pickle', 'wb') as f:
            pickle.dump(self.options, f)

    # Cognitive senses: speaking, listening, seeing
    def speak(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()
        print(self.name + ": " + phrase)
        return phrase

    def listen(self):
        if self.options['input'] == 'speech':
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

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

    def vision(self):
        pass

    def switch_input(self):
        if self.options['input'] == 'keyboard':
            self.options['input'] = 'speech'
        else:
            self.options['input'] = 'keyboard'

    def activate(self):
        statement = self.listen().lower()
        if 'nebula' in statement:
            self.activated = True

    def edit_options(self, obj):
        self.options = obj
        self.save_options()
        return self.options

    def change_password(self, new_password, old_password):
        if old_password == self.password:
            self.password = new_password
            self.speak('password updated...')

    def request_password(self, input_password):
        if input_password == self.password:
            return True
        else:
            return False

    def brain(self, statement):
        if statement is not None or statement != '':
            intent = Actions().get_intent(statement)

            if intent == 'stop_assistant':
                self.activated = False

            response = Actions().analyze_statement(statement)
            self.speak(response)
        else:
            self.silent_notice += 1
            if self.silent_notice == 5:
                print('going to sleep...')
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


nebula = Assistant()
nebula.start()
