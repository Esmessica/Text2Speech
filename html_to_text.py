import pyttsx3
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init()

user_url = input("Enter your URL: ")
name_file = input("How is your finnished file gonna be named? (file will be in .txt document) ")
responce = requests.get(f"{user_url}")
web = responce.text
soup = BeautifulSoup(web, "html.parser")

article = soup.find_all("p")
file_name = f"coda_run{name_file}"


with open(f"{file_name}.txt", "w", encoding="utf-8") as web_file:
    for one_article in article:
        one_article_text = one_article.get_text()
        print(".")
        web_file.write(one_article_text)
        web_file.write("\n")

        engine.setProperty("rate", 120)
        engine.say(one_article_text)
        engine.runAndWait()

"""TODO:
    1) OOP whole project
    2) make it choose scarping web or using donwloaded pdf/txt file
    3) try to solve language issue
    4) pack whole project to instalable file
    """