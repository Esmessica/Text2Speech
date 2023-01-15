import pyttsx3


class FileHandler:

    def user_file_input(self):
        self._file_name = input("Enter desired name for new file: ")

        """ self._file_name = f"{self._file_input}_code" """

    def file_handler(self):

        with open(f"{self._file_name}.txt", "w", encoding="utf-8") as web_file:
            for one_article in self._text_to_write:
                one_article_text = one_article.get_text()
                print(".")
                web_file.write(one_article_text)
                web_file.write("\n")

    def file_test(self):
        engine = pyttsx3.init()
        reader = PdfReader("spalovac_mrtvol.pdf")
        number_of_pages = reader.numPages
        page = reader.pages[0]

        for i in range(reader.numPages):
            page = reader.pages[i]

        text = page.extractText()
        engine.say(text)
        engine.runAndWait()
        engine.save_to_file(text, 'test.mp3')

"""
        with open(f"{self._file_name}.pdf", "r") as web_file:
            webs = web_file.read()
            engine = pyttsx3.init()
            engine.say(webs)
            engine.runAndWait()"""





"""engine = pyttsx3.init()
reader = PdfReader("spalovac_mrtvol.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[10]

for i in range(len(reader.pages)):
    page = reader.pages[i]

text = page.extract_text()
engine.say(text)
engine.runAndWait()
engine.save_to_file(text, 'test.mp3')
"""


