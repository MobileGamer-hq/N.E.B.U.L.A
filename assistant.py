# import all the modules needed
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
import lists
import functions
import data
from playsound import playsound

class Assistant:

    # This is used to pick random responses from the list to be used by sophie
    HAU = lists.HAU
    compliment = functions.compliment
    coin = lists.coin
    dice = lists.dice
    Page = lists.Page
    IWT = lists.IWT

    assistData = data.data
    spoken_words = ""
    conversations = []#list(data.loadData("conversations.json"))


    def Start(self):
        assistData = data.loadData()
        P_HAU = random.choice(self.HAU)
        P_IWT = random.choice(self.IWT)
        P_compliment = random.choice(self.compliment)
        flip = random.choice(self.coin)
        roll = random.choice(self.dice)
        PO = random.choice(self.Page)


        # Ignore all warnings during the run of the code
        warnings.filterwarnings('ignore')

        # Giving it the ability to
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        # This is used to make N.B.U.L.A speak
        def speak(text):
            engine.say(text)
            engine.runAndWait()
            self.spoken_words = text


        # This is the greeting which she will choose from depending on the time of day
        def wishMe():
            hour = datetime.datetime.now().hour
            if hour >= 0 and hour < 12:
                speak("Good Morning")
                print("Good Morning")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon")
                print("Good Afternoon")

            else:
                speak("Good Evening")
                print("Good Evening")

        wishMe()


        # defining the take command for speech_recognition
        def takeCommand():
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

                try:
                    statement = r.recognize_google(audio, language='en-in')
                    print(': ' + statement)

                except Exception as e:
                    speak("please say that again")
                    return "None"
                return statement

        if __name__ == 'assistant':

            while True:
                data.saveData(assistData)
                speak("what can i do for you?")
                statement = takeCommand().lower()
                
                if statement == 0:
                    continue

                #This will stop the operation 
                if "good bye" in statement or "ok bye" in statement or "stop" in statement or 'goodbye' in statement or 'bye' in statement or 'thanks' in statement or 'thank you' in statement or 'nothing' in statement or 'go away' in statement:
                    speak('okay, goodbye')
                    print('OK')
                    break

                elif "your name" in statement or "who are you" in statement or "what is your name" in statement:
                    speak("I am Nebula")
                    print("I am Nebula")

                elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I was built by Mobile Gamer")
                    print("I was built by MobileGamer")

                elif "what did i say" in statement:
                    speak(statement)
                    print(statement)

                elif "why do i programme" in statement or "why do i code" in statement:
                    speak("because you are good at it and thats what you are")
                    print(":) you are a great programmer")

                # Search on wikipedia
                elif 'wikipedia' in statement or 'search' in statement or "who is" in  statement:
                    speak('Searching Wikipedia...')
                    result = functions.SearchWiki(statement)
                    speak("According to Wikipedia")
                    print(result)
                    speak(result)
                
#All code for openning websites goes here

                # Open youtube
                elif 'open youtube' in statement:
                    functions.OpenPage("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                # open google
                elif 'open google' in statement:
                    functions.OpenPage("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)

                # open google mails
                elif 'open gmail' in statement:
                    functions.OpenPage("https://mail.google.com/mail/u/0/#inbox")
                    speak("Google Mail is open now")
                    time.sleep(5)

                # open google news
                elif 'news' in statement:
                    functions.OpenPage("https://news.google.com/topstories?hl=en-NG&gl=NG&ceid=NG:en")
                    speak('Here are some headlines from Google')
                    time.sleep(6)

                # Open google maps
                elif 'open map' in statement:
                    functions.OpenPage('https://maps.google.com/')
                    speak('google maps is open now')
                    print('Opening.....')

                # open google translator
                elif 'open translator' in statement or 'translate' in statement:
                    functions.OpenPage('https://translate.google.com/')
                    speak('Google translator is open now')
                    print('opening')

                # Open google photos
                elif 'open photos' in statement or 'photos' in statement:
                    functions.OpenPage('https://photos.google.com/?tab=rq&pageId=none')
                    speak('google photos is open now')
                    print('opening')

                # Open google drive
                elif 'open drive' in statement or 'google drive' in statement:
                    webbrowser.open('https://drive.google.com/drive/u/0/my-drive')
                    speak('google drive is open now')
                    print('opening')

                # Open google keep
                elif 'open keep' in statement or 'google keep' in statement:
                    webbrowser.open('https://keep.google.com/u/0/#home')
                    speak('google keep is open now')
                    print('opening')

                # Open google docs
                elif 'open docs' in statement or 'google documents' in statement or 'google docs' in statement:
                    webbrowser.open('https://docs.google.com/document/u/0/')
                    speak("google docs is open now")
                    print('opening')

                # Open google sites
                elif 'open sites' in statement or 'open site' in statement or 'open web' in statement:
                    webbrowser.open('https://sites.google.com/u/0/new/?authuser=0')
                    speak("google sites is open now")

#All code that have to do with responses goes here

                # tell me the time
                elif 'time' in statement:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                    print(strTime)

                elif "compliment" in statement or "tell me a compliment" in statement:
                    speak(P_compliment)
                    print(P_compliment)

                elif 'calculate' in statement or 'can you calculate' in statement:
                    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                    question = takeCommand()
                    app_id = "Paste your unique ID here "
                    client = wolframalpha.Client('WPJJUY-98262EP8PR')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)

                elif "how are you" in statement:
                    speak(P_HAU)
                    print(P_HAU)

                elif 'open my blog' in statement:
                    webbrowser.open_new_tab("https://mobilegamerhq.blogspot.com/")
                    speak("your blog is open now")
                    time.sleep(5)

                elif 'open YT music' in statement or 'play music' in statement or 'vibing' in statement:
                    webbrowser.open_new_tab("https://music.youtube.com/playlist?list=PLCRCtthPFnxGLZdOS84qpAihJFdN1t7BH")
                    speak("Youtube music is open now")
                    time.sleep(5)

                elif 'flip a coin' in statement or 'flip a' in statement:
                    speak('it landed on' + flip)
                    print(flip)

                elif 'roll a dice' in statement or 'roll a' in statement:
                    speak('it landed on' + roll)
                    print(roll)

                elif 'open a random page' in statement:
                    webbrowser.open_new_tab(PO)
                    speak("a random page from your blog has been open")

                elif 'start bot' in statement or 'bot' in statement or 'start' in statement:
                    webbrowser.open(PO)
                    speak('your bot has started')
                    print('......')

                elif 'i want to talk' in statement:
                    speak(P_IWT)
                    print(P_IWT)

                elif 'project' in statement:
                    webbrowser.open('https://app.milanote.com/1Kt24Q10CTqsET/home')
                    speak('you can now start your project')
                    print('opening.....')

                elif "all projects" in statement or "all project" in statement:
                    webbrowser.open("https://app.milanote.com/1KRLhg12dNeX0G/projects?p=YvGGoS8AKhM")
                    speak("showing all projects available")
                    print("showing all projects")

                elif 'nebula' in statement or 'hello' in statement:
                    speak('hello mobile gamer')
                    print('Hello MobileGamer')

                elif 'check my youtube' in statement or 'my youtube' in statement:
                    webbrowser.open(
                        'https://studio.youtube.com/channel/UCvSMyEi2iMOkz10ae9kaY7Q/analytics/tab-overview/period-default')
                    speak(
                        'you can now check your youtube analytics')
                    print(
                        'opening stats.....')

                elif 'check my blog' in statement or 'my blog' in statement:
                    webbrowser.open('https://analytics.google.com/analytics/web/#/report-home/a174200105w241674239p225387149')
                    speak(
                        'you can now check the analytics of your blog')
                    print(
                        'opening stats.....')

                elif 'school' in statement or 'start school' in statement or 'open school' in statement:
                    webbrowser.open('https://whitesands-ss.edupage.org/user/?')
                    speak(
                        'are you ready for school?')
                    print(
                        'opening edupage.....')

                elif 'what can you do' in statement or 'can you do' in statement:
                    speak(
                        'I can search on wikipedia, open youtube, google, gmail, tell you the time, check how your site, codes and videos are doing, tell you the latest news and help you with school')
                    print(
                        'I can search on wikipedia, open youtube,  google, gmail, tell you the time, check how your site, codes and videos are doing, tell you the latest news and help you with school')

                elif 'command one' in statement or 'command 1' in statement:
                    print(
                        'open google, open youtube, open gmail, open translator, open maps, open school, check my code, check my blog, check my youtube, blog, play music, time, search for, wikipedia')
                    speak(
                        'open google, open youtube, open gmail, open translator, open maps, open school, check my code, check my blog, check my youtube, blog, play music, time, search for, wikipedia')
                    time.sleep(5)

                elif 'how to' in statement or 'how do you' in statement:
                    webbrowser.open_new_tab(statement)
                    speak('searching for '+statement)
                    print('Searching.....')

                elif "design" in statement or "designs" in statement:
                    webbrowser.open("https://designer.gravit.io/")
                    speak("opening your designs")
                    print("opening.....")

                elif "learn" in statement or "learn code" in statement:
                    webbrowser.open("https://www.sololearn.com/learning")
                    speak("which language will you like to learn")
                    print("opening.....")

#all code for changing and checking the content of list goes here

                elif "how many villains in my list" in statement or "how many villains" in statement or "count the number of villains" in statement:
                    villanCount = len(list.villains)
                    speak(villanCount)
                    print(villanCount)

                elif "to my list of villains" in statement or "to my villain list" in statement or "to villains" in statement or "to my villains" in statement:
                    statement = statement.replace("add","")
                    statement = statement.replace("to","")
                    statement = statement.replace("my","")
                    statement = statement.replace("list","")
                    statement = statement.replace("of","")
                    statement = statement.replace("villains","")
                    statement = statement.replace("villain","")

                    list.villains.append(statement)
                    functions.addVillains()

                    speak("adding")
                    print(list.villains)


                elif "how many targets in my list" in statement or "how many targets" in statement or "count the number of targetss" in statement:
                    targetCount = len(list.target)
                    speak(targetCount)
                    print(targetCount)

                elif "to my list of targets" in statement or "to my target list" in statement or "to targets" in statement or "to my targets" in statement or "to target" in statement:
                    statement = statement.replace("add","")
                    statement = statement.replace("to","")
                    statement = statement.replace("my","")
                    statement = statement.replace("list","")
                    statement = statement.replace("of","")
                    statement = statement.replace("targets","")
                    statement = statement.replace("target","")

                    list.target.append(statement)
                    functions.addTarget()

                    speak("Adding.....")
                    print("Adding.....")
                    print(list.target)

                
                #all aplication opennning code goes here
                elif "open visual studio code" in statement or "i want to programme" in statement or "visual studio code" in statement or "visual studio" in statement:
                    speak("openning visual studio code")
                    print("openning.....")
                    subprocess.call("C:\\Users\KINGSLEY-DURU\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

                elif "open unity" in statement:
                    speak("openning unity hub")
                    print("openning.....")
                    subprocess.call("C:\\Program Files\\Unity Hub\\Unity Hub.exe")

                elif "open calculator" in statement:
                    speak("openning calculator")
                    print("openning.....")
                    subprocess.call("calc.exe")
                    

                elif "open rider" in statement:
                    speak("openning Rider")
                    print("openning.....")
                    subprocess.call("C:\\Users\\KINGSLEY-DURU\\AppData\\Local\\JetBrains\\Toolbox\\apps\\Rider\\ch-0\\213.6775.4\\bin\\rider64.exe")


                elif "add to my to do" in statement or "to do" in statement or "todo" in statement:
                    statement = statement.replace("add","")
                    statement = statement.replace("to","")
                    statement = statement.replace("my","")
                    statement = statement.replace("to","")
                    statement = statement.replace("do","")
                    lists.ToDo.append(statement)
                    speak("adding to to do")
                    print("Adding to ToDo")

                values = {
                    "you": statement,
                    "nebula": self.spoken_words,
                }

                self.conversations.append(values)

                whatYouSaid = open("statement.txt","w")
                whatYouSaid.write(str(self.conversations))

                data.saveData(self.conversations, "conversations.json")