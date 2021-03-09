import time
import datetime
import os
from gtts import gTTS
import pyttsx3

engine = pyttsx3.init()

print("Ce vrei sa-ti aduc aminte?")
motiv = str(input("Motivul reminderului: "))
durata = float(input("In cate minute sa-ti aduc aminte? "))
time.sleep(durata*60)

for i in range(5):
    print(motiv)
    time.sleep(2)
    #os.system("start audio.mp3")
    engine.setProperty("rate", 178)
    engine.say(motiv)
    engine.runAndWait()


#lang = 'en'

#myobj = gTTS(text=text, lang=lang, slow=False)
#myobj.save("audio.mp3")


