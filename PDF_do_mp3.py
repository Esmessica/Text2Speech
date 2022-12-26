import PyPDF2
import gtts
from playsound import playsound

print("\tEnter name of your desired file below.\n(Please remember that file has to be in same"
      " folder with this program OR enter path to file-example below)\n")
print("Example of path: 'C:/Users/my_name/Desktop/NAME_OF_PDF_FILE'\n")

pdf_file = input("PDF: ")

path = open(f"{pdf_file}.pdf", "rb")


reader = PyPDF2.PdfReader(path)
frompage = reader.pages[1]
text = frompage.extract_text()
tts = gtts.gTTS(f"{text}", lang="cs")
file_name = f"{pdf_file}"

if "_" in pdf_file:
      f = file_name.replace("_", "")
      tts.save(f"{f}.mp3")
else:
      tts.save(f"{pdf_file}.mp3")
    #  playsound(f"{pdf_file}.mp3")