import PyPDF2
import gtts
import pdfplumber


print("\tEnter name of your desired file below.\n(Please remember that file has to be in same"
      " folder with this program OR enter path to file-example below)\n")
print("Example of path: 'C:/Users/my_name/Desktop/NAME_OF_PDF_FILE'\n")

try:
    pdf_file = input("PDF: ")
    path = open(f"{pdf_file}.pdf", "rb")
    reader = PyPDF2.PdfReader(path)

    num_pages = 0
    for page in path:        # counts pages
        num_pages = num_pages + 1
        frompage = len(reader.pages)

    print(f"{num_pages} pages long document")

    if 5 < num_pages < 50 :
        print("This file is abit long, might take a moment")
    elif num_pages > 50:
        print("This might take some time, make yourself comfy")  # prints sentence based on lenght of pdf

    text = frompage.extract_text()
    tts = gtts.gTTS(f"{text}", lang="cs")
    file_name = f"{pdf_file}"

    if "_" in pdf_file:     # decision for shortening final mp3 file
        f = file_name.replace("_", "")
        tts.save(f"{f}.mp3")

    else:                   # code that runs if _ is not in file name
        tts.save(f"{pdf_file}.mp3")

    print("\nDone")

except FileNotFoundError:    # error for not existing file name
    print("This file seems to not exist.")



# add code for picking page
# make multiple pages chooser