import os
import pyaudio
import calendar
import json
import requests
import subprocess
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import warnings
import speech_recognition as sr
import random
import wolframalpha
import openai
from playsound import playsound


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
        pass

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
                statement = recognizer.recognize_google(
                    audio, language='en-in')
                print(': ' + statement)

            except Exception as exc:
                self.speak("please say that again")
                return "None"
        return statement


    def process_with_gpt(input_text):
        # Authenticate with the OpenAI API
        openai.api_key = "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"

        # Set the model and parameters
        model_engine = "text-davinci-002"
        prompt = input_text
        temperature = 0.5
        max_tokens = 60

        # Generate text using GPT-3
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Return the generated text
        return response.choices[0].text

    def brain(self, statement):
        if "hello" in statement or "hi" in statement or "nebula" in statement:
            self.speak('Good day sir.')

        elif "whats the time" in statement:
            self.speak('Good day sir.')

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
