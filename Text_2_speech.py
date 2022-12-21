import pyttsx3
from bs4 import BeautifulSoup
import requests
from random import randint
engine = pyttsx3.init()
responce = requests.get("https://packaging.python.org/en/latest/tutorials/packaging-projects/")
web = responce.text
soup = BeautifulSoup(web, "html.parser")

article = soup.find_all(id ="packaging-python-projects")
file_name = f"coda_run{randint(1,356)}"
with open(f"{file_name}.txt", "w", encoding="utf-8") as web_file:
    for one_article in article:
        one_article_text = one_article.get_text()
        print("+1")
        web_file.write(one_article_text)
        web_file.write("\n")

        engine.setProperty("rate", 120)
        engine.say(one_article_text)
        engine.runAndWait()

