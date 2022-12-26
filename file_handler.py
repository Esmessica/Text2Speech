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
        with open(f"{self._file_name}.txt", "r", encoding="utf-8") as web_file:
            webs = web_file.read()
            engine = pyttsx3.init()
            engine.say(webs)
            engine.runAndWait()


f = FileHandler()
f.user_file_input()
f.file_test()

