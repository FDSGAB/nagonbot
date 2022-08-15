import requests
from bs4 import BeautifulSoup

URL = "https://hgbrasil.com/status/weather"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mainContent")

#print(results.prettify())

temperature_elements = results.find_all("div", class_="_flex _align-center _relative")

for element in temperature_elements:
    temp_number = element.find_all("span", class_= "temperature _margin-l-5 -font-13")
print(temp_number)