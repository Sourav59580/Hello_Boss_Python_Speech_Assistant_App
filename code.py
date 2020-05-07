import speech_recognition as sr
import pyttsx3
from time import ctime
import time
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source :
        if ask :
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try :
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError :
            print("Sorry boss ! I did not get that")
            speak("Sorry boss ! I did not get that")
        except sr.RequestError :
            print("Sorry boss ! my speech service is down now")
            speak("Sorry boss ! my speech service is down now")
        return voice_data

def respond(voice_data) :
    if 'what is your name' in voice_data :
        print('My name is Tarzan')
        speak('My name is Tarzan')

    if 'what time is it' in voice_data :
        print(ctime())
        speak(ctime())

    if 'search' in voice_data :
        speak("What do you want to search for?")
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is what i found for "+ search)
        print("Here is what i found for "+ search)

    if 'find location' in voice_data :
        speak("What is the location?")
        location = record_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak("Here is the location of "+ location)
        print("Here is the location of "+ location)

# speak function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

time.sleep(1)
print("How can I help you?")
speak('How can I help you?')
while 1 :
    voice_data = record_audio()
    respond(voice_data)

