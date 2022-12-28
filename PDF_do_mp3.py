import PyPDF2
import pyttsx3
import pdfplumber

# printing information for start
print("\tEnter name of your desired file below.\n(Please remember that file has to be in same"
      " folder with this program OR enter path to file-example below)\n")
print("Example of path: 'C:/Users/my_name/Desktop/NAME_OF_PDF_FILE'\n")

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

    """num_pages = 0
    for page in path:            # counts pages
        num_pages = num_pages + 1
        frompage = len(reader.pages)
    print(f"{num_pages} pages long document")

    if 5 < num_pages < 50 :
        print("This file is abit long, might take a moment")
    elif num_pages > 50:
        print("This might take some time, make yourself comfy")  # prints sentence based on lenght of pdf
    """
    """    #  text = frompage.extract_text()           # library for saving file start of code
    tts = gtts.gTTS(f"{final_text}", lang="cs")       # tts = gtts.gTTS(f"{text}", lang="cs")
    file_name = f"{pdf_file}"

    if "_" in pdf_file:     # decision for shortening final mp3 file
        f = file_name.replace("_", "")
        tts.save(f"{f}.mp3")

    else:                   # code that runs if _ is not in file name
        tts.save(f"{pdf_file}.mp3")"""

    engine = pyttsx3.init()
    engine.save_to_file(final_text, f"{pdf_name}.mp3")
    engine.runAndWait()

    print("\nDone")

except FileNotFoundError:    # error for not existing file name
    print("This file seems to not exist.")


# add code for picking page
# use two versions of libraries based on language decision