import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from tkinter import *

listener=sp.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sp.Microphone() as source:
            print("listening......")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "assistant" in command:
                command=command.replace("assistant","")
    except:
        print("error")
    return command

def runmain():
    command=take_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        print("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is "+time)
        print("Current time is "+time)
    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,3)
        talk(info)
        print(info)
    elif "what is" in command:
        thing=command.replace("what is","")
        inform=wikipedia.summary(thing,3)
        talk(inform)
        print(inform)
    elif "joke" in command:
        joke=pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif ["hi","hello","hey","hai","good"] in command:
        talk("hey,I will always help you")
        print("hey,I will always help you")
    elif "how are you" in command:
        talk("I am fine,thank you  hope you are fine")
        print("I am fine,thank you  hope you are fine")
    else:
        talk("oops it is not clear")
        print("oops it is not clear")


while True:
    runmain()
