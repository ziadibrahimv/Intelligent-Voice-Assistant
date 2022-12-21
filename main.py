import pyttsx3 as p
import speech_recognition as sr

from selenium_web import infow
from Scripts.YT_auto import *

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("good morning ziad !")
    elif hour>= 12 and hour<18:
        speak("good Afternoon fakhr !")
    else:
        speak("good evening ziad !")

engine = p.init()
rate=engine.getProperty('rate')
engine. setProperty ('rate' ,150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello sir i am your voice assistant. how are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak ("i am having a good day sir")
speak ("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)


if "information" in text2:
    speak("you information related to which topic")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
    speak("what do you want to watch??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("playing {} on youtube".format(vid))
    speak("playing {} on youtube".format(vid))

    assist = music()
    assist.play(vid)

