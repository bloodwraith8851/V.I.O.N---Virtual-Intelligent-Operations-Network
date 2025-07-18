import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows, 'espeak' for Linux
    voices = engine.getProperty('voices')
#    print("Available voices:",voices)
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 180)  # Set speech rate
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10 , 6 )# 10 seconds timeout for audio input from the user and 6 seconds for speech recognition
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
#        time.sleep(2)
#        speak(query)
#        eel.ShowHood()
    except Exception as e:
        return ""
    return query.lower()

#text = takecommand()

#speak(text)

@eel.expose
def allCommands():
    try:
        query = takecommand()
        print(query)
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("Not opening...")
    except:
        print("Error")
    
    eel.ShowHood()