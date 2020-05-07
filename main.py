import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    print("Say something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("voice",voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Sourav is a good boy")