import requests
from bs4 import BeautifulSoup


url = "https://www.worldometers.info/coronavirus/"

html = requests.get(url).text
soup = BeautifulSoup(html,features="html.parser")
numbers = soup.find_all(attrs={"class": "maincounter-number"})

total = numbers[0].text.strip()
deaths = numbers[1].text.strip()
recovered = numbers[2].text.strip()
print("Total cases: " + total)
print("Total Deaths: " + deaths)
print("Total Recovered: " + recovered)
