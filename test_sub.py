import PyPDF2
import gtts
import pdfplumber
from playsound import playsound

file = "spalovac_mrtvol.pdf"

book = open(file, "rb")
pdf_reader = PyPDF2.PdfReader(book)
pages = len(pdf_reader.pages)
final_text = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        final_text += text
tts = gtts.gTTS(f"{final_text}", lang="cs")
tts.save("hello.mp3")
playsound("hello.mp3")