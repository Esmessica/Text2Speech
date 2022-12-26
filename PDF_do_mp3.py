import PyPDF2
import gtts
from playsound import playsound


path = open("spalovac_mrtvol.pdf", "rb")
reader = PyPDF2.PdfReader(path)
frompage = reader.pages[144]
text = frompage.extract_text()
tts = gtts.gTTS(f"{text}", lang="cs")
tts.save("hello.mp3")
playsound("hello.mp3")