import requests
from bs4 import BeautifulSoup

search_term = "木"
url = "https://www.weblio.jp/content/" + search_term



page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(class_="kijiWrp") #Results é uma lista com todos os artigos relacionados à palavra do website. Definição, dicionário de kanji etc.



titles = soup.find_all(class_ = "midashigo")
for titl in titles:
    print(titl.prettify())
descriptions = soup.find_all(class_ = "Sgkdj")
number_list = list()
for description in descriptions:
    numbers = description.find_all("b")
    if not numbers:  #verifica se a lista esta vazia ou nao
        number_list.append(1)
        continue
    for number in numbers:
        try:
            number_list.append(int(number.text))
        except:
            continue
print(number_list)

print(len(number_list))

for i in range (0,len(number_list)):
    if number_list[i]==1:
        print(titles[i].text)
        print(descriptions[i].text)
