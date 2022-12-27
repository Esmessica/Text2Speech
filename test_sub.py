import PyPDF2
import pyttsx3
import pdfplumber
import time
from playsound import playsound
now = time.time()
file = "romeo.pdf"
book = open(file, "rb")
pdf_reader = PyPDF2.PdfReader(book)
pages = len(pdf_reader.pages)
final_text = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        final_text += text
engine = pyttsx3.init()
engine.save_to_file(final_text, "test.mp3")
engine.runAndWait()
minus = time.time()

print("DONE")
print(f"Took {int(minus - now)} seconds to finnish")
