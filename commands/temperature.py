import requests
from bs4 import BeautifulSoup
from func.Speak import speak


def taapmaan():
    search = "temperature in Hisar"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    print(f"ULTRON : Current {search} is {temp}")
    speak(f"current{search} is {temp}")






