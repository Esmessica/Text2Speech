import PyPDF2
import pyttsx3
import pdfplumber
from playsound import playsound

file = "romeo.pdf"
book = open(file, "rb")
pdf_reader = PyPDF2.PdfReader(book)
pages = len(pdf_reader.pages)
final_text = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, 50):       # pages
        page = pdf.pages[i]
        text = page.extract_text()
        final_text += text
engine = pyttsx3.init()
engine.save_to_file(final_text, "test.mp3")
engine.runAndWait()

print("DONE")