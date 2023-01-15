# google text to speech
"""import gtts
from playsound import playsound

tts = gtts.gTTS("AHoj šmejde", lang="cs")
tts.save("hello.mp3")
playsound("hello.mp3")
"""

# python text to speech
import pyttsx3


engine = pyttsx3.init()
file_in = open("test.txt", "r")
engine.say(file_in)
engine.runAndWait()

"""
engine = pyttsx3.init("dummy")
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
"""

"""engine = pyttsx3.init()
text = "Python is a great programming language"
engine.say(text)
engine.say("Hi")
# play the speech
engine.runAndWait()
rate = engine.getProperty("rate")
print(rate)
voices = engine.getProperty("voices")
print(voices)"""