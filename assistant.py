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


class Assistant:
    name = "nebula"
    password = ""
    key = ""
    engine = pyttsx3.init('sapi5')
    activated = False

    def __init__(self) -> None:

        # Ignore all warnings during the run of the code
        warnings.filterwarnings('ignore')

        # Giving it the ability to speak
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        self.options = data.get_json('data/assistant_options.json')
        if self.options === None:
            self.options = {
                'user': null,
            }

    # cognitive senses speaking, listening, seeing
    def speak(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()
        print(phrase)
        return phrase

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                statement = recognizer.recognize_google(audio, language='en-in')
                print(': ' + statement)
            except Exception as exc:
                self.speak("please say that again")
                return "None"
            
        return statement

    def brain(self, statement):
        intent = actions.get_intent(statement)

        if intent === "greeting":
            print('')

    def start(self):
        if __name__ == "__main__":
            while self.activated == True:

                statement = self.listen().lower()
                self.speak("What can I do for you?")

                whatYouSaid = open("statement.txt", "w")
                whatYouSaid.write(statement)
                whatYouSaid.close()

                if statement == 0:
                    continue
                else:
                    self.brain(statement)

nebula = Assistant()
text = nebula.listen()
print(text)