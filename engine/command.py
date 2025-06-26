import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows, 'espeak' for Linux
    voices = engine.getProperty('voices')
    print("Available voices:",voices)
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 180)  # Set speech rate
    engine.say(text)
    engine.runAndWait()

speak("Hello, this is a test of the text-to-speech engine.")