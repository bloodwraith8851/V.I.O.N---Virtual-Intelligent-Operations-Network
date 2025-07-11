import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import Assistant_Name
import pywhatkit as kit
import re
import sqlite3
import webbrowser
import pvporcupine
import struct
import pyaudio
import time
from engine.helper import extract_yt_term

conn = sqlite3.connect('vion.db')
cursor = conn.cursor()

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
    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
    
    # if query!="":
    #     speak ("Opening "+query)
    #     os.system("start "+query)
    # else:
    #     speak("not found")

# youtube command

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing " + search_term + " on youtube")
    kit.playonyt(search_term)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        #pre trained keywords
        porcupine=pvporcupine.create(keywords=["vion","vi"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        #loop for streaming
        while True:
            keyword=audion_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword) 