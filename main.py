import datetime
import os
import webbrowser

import speech_recognition
import pyttsx3
import wikipedia
import pyaudio
import openai



engine=pyttsx3.init('sapi5')#this sapi5 will get the voices from the desktop
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour<=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am your charo. please tell me how can i help you")

def takecommand():

      #it takes the microphone input from the user
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
          print("listening...")
          r.pause_threshold=1
          audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("please say again")
        return "none"
    return query

if __name__ == '__main__':
    #speak("dilliram is a good boy")
    wishMe()
    while True:
        query=takecommand().lower()

        #how to execute task based query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia'," ")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif ' youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif ' open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            path="C:\\Users\\dilli\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)
        elif'the time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'open pycharm' in query:
            codePath="D:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\pycharm64.exe"
            os.startfile(codePath)
        elif 'open openai' in query:
            webbrowser.open("openai.com")
        elif 'clear the current folder' in query:
            exit()



