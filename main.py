# google text to speech
"""import gtts
from playsound import playsound

tts = gtts.gTTS("AHoj šmejde", lang="cs")
tts.save("hello.mp3")
playsound("hello.mp3")
"""

import pyttsx3
import PyPDF2

engine = pyttsx3.init()
file_in = open("spalovac_mrtvol.pdf", "rb")
read_pdf = PyPDF2.PdfReader(file_in, strict=False)
number_of_pages = len(read_pdf.pages)

for i in range(3, number_of_pages):
    # Read the PDF page
    page = read_pdf.pages[i]
    # Extract the text of the PDF page
    page_content = page.extract_text()

    engine.say(page_content)

    engine.runAndWait()
    coun = 0
    print(f"Page: {coun + 1}")

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