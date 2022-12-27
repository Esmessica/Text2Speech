import PyPDF2
import gtts
# from playsound import playsound


print("\tEnter name of your desired file below.\n(Please remember that file has to be in same"
      " folder with this program OR enter path to file-example below)\n")
print("Example of path: 'C:/Users/my_name/Desktop/NAME_OF_PDF_FILE'\n")

try:
    pdf_file = input("PDF: ")
    path = open(f"{pdf_file}.pdf", "rb")
    reader = PyPDF2.PdfReader(path)

    pocet = 0
    for strana in path:        # counts pages
        pocet = pocet + 1

    print(f"{pocet} pages long document")

    if 5 < pocet < 50 :
        print("This file is abit long, might take a moment")
    elif pocet > 50:
        print("This might take some time, make yourself comfy")

    frompage = reader.pages[2]
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