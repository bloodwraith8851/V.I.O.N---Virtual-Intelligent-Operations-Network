import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import Assistant_Name
import pywhatkit as kit
import re

# play assistant sound

@eel.expose
def playassistantsound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

# open command

def openCommand(query):
    query = query.replace(Assistant_Name,"")
    query = query.replace("open","")
    query.lower()
    
    if query!="":
        speak ("Opening "+query)
        os.system("start "+query)
    else:
        speak("not found")

# youtube command

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing " + search_term + " on youtube")
    kit.playonyt(search_term)

# extract search term

def extract_yt_term(command):
    # Regular expression pattern to extract the search term
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Search for the pattern in the command 
    match = re.search(pattern, command, re.IGNORECASE)
    # Return the search term if found and None otherwise 
    return match.group(1) if match else None