import PyPDF2
import pyttsx3
import pdfplumber
import time


now = time.time()       # start of application timer

pdf_name = input("Enter pdf name (must be in same folder as this application file)\n_ ")
file = f"{pdf_name}"

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
engine.save_to_file(final_text, f"{pdf_name}.mp3")
engine.runAndWait()

minus = time.time()  # end of application time

print("DONE")
print(f"Took {int(minus - now)} seconds to finnish")
