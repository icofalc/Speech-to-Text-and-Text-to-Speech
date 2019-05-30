import speech_recognition as sr

from gtts import gTTS
import subprocess

r = sr.Recognizer()


print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)

with mic as source:
    r.adjust_for_ambient_noise(source) 
    audio4 = r.listen(source)

try:
    text = r.recognize_google(audio4,language="it-IT")
    print(text)
except sr.RequestError:
    print( "API unavailable" )
except sr.UnknownValueError:
    print( "Unable to recognize speech" )



tts = gTTS(text=text, lang='it')

tts.save("tts_output_audio.mp3")

print("tutto fatto, file salvato!")
print("eseguo il run dell'audio")
subprocess.run(["afplay", "tts_output_audio.mp3"])

import os
os.remove("tts_output_audio.mp3")
print("file eliminato!")
