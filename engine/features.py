from playsound import playsound
import eel
@eel.expose
def playassistantsound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)