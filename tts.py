from gtts import gTTS
from playsound import playsound
import pyttsx3
def speech(text):
    try:
        engine = pyttsx3.init()

        engine.say(text)
        engine.runAndWait()
        engine.stop()
        engine.endLoop()
    except Exception as err:
        return "Error Log:[{}]".format(err)