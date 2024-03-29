import PyPDF2
import pyttsx3
import pdfplumber
import time


now = time.time()       # start of application timer

# printing information for start
print("\tEnter name of your desired file below.\n(Please remember that file has to be in same"
      " folder with this program OR enter path to file-example below)\n")
print("Example of path: 'C:/Users/my_name/Desktop/NAME_OF_PDF_FILE'\n")

# Main part of PDF to MP3 file app
try:
    pdf_name = input("PDF: ")
    file = f"{pdf_name}"

    path = open(f"{file}.pdf", "rb")
    reader = PyPDF2.PdfReader(path)
    pages = len(reader.pages)

    final_text = ""

    with pdfplumber.open(f"{file}.pdf") as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            final_text += text

    if 5 < pages < 50:
        print("This file is abit long, might take a moment")
    elif pages > 50:
        print("This might take some time, make yourself comfy")  # prints sentence based on lenght of pdf

    if "_" in pdf_name:     # decision for shortening final mp3 file
        f = file.replace("_", "")

    else:                   # code that runs if _ is not in file name
        f = file

    engine = pyttsx3.init()
    engine.save_to_file(final_text, f"{f}.mp3")
    engine.runAndWait()
    minus = time.time()  # end of application time

    print("\nDone")
    print(f"Took {int(minus - now)} seconds to finnish")

except FileNotFoundError:    # error for not existing file name
    print("This file seems to not exist.")
