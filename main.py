# import libraries
from mimetypes import init
import os
import random
import webbrowser
import datetime
import speech_recognition as sr
import pyttsx3

# Exceptions
class NullQueryException(Exception):
    pass
# user profile and authentication

class User(object):
    __user_name = "Amit"
    __user_pass = "pigeon"

    def get_name(self):
        return self.__user_name
    def set_name(self, name):
        self.__user_name = name 
    def set_password(self, password):
        self.__user_pass = password
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(User, cls).__new__(cls)
        return cls.instance
    
    

class VA(object):
    __user_name = "Doodle"
    __user_pass = "dude"

    def get_name(self):
        return self.__user_name
    def set_name(self, name):
        self.__user_name = name 
    def set_password(self, password):
        self.__user_pass = password
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VA, cls).__new__(cls)
        return cls.instance

class Counter:
    value = 0
    def __init__(self, seed=0):
        self.value += seed
    def __call__(self, val=None):
        if not val:
            self.value += 1
        else:
            self.value += val
    def reset(self):
        self.value = 0
    

def speak_up(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    clock = int(datetime.datetime.now().hour)
    if clock>=6 and clock<12:
        speak_up("Good Morning")
    elif clock>=12 and clock<18:
        speak_up("Good Afternoon")
    elif clock>=18 and clock<24:
        speak_up("Good Evening")
    else:
        speak_up("Any Command Sir")

def get_command(user,va):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{va.get_name()}: Listening... ... ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(f"{va.get_name()}: Processing... ... ...")
        query = r.recognize_google(audio, language='en-us')
        if not query:
            raise NullQueryException
        print(f"{user.get_name()}: {query}")
    except NullQueryException:
        speak_up("No input found")
    except sr.UnknownValueError:
        query = None
    return query
def take_action(query):
    if 'wikipedia' in query:
        speak_up("searching is wiki")

if __name__ == '__main__':
    # initial setup
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    user = User()
    assistant = VA()
    print("Voice Assistant is active\n\n")
    speak_up(f"Hi {user.get_name()}")
    greetings()
    count = Counter()
    while True:
        if not count.value == 5:
            q = get_command(user,assistant)
        else:
            break
        if not q:
            count()
            continue
        take_action(q)