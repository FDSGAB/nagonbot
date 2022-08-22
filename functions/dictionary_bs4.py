import requests
from bs4 import BeautifulSoup
from .voice import voice_answer

def get_word_dic (engine):
    voice_answer("検索したい言葉を教えてください: ", engine)
    search_term = input()
    url = "https://www.weblio.jp/content/" + search_term


    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="kijiWrp") #Results é uma lista com todos os artigos relacionados à palavra do website. Definição, dicionário de kanji etc.



    titles = soup.find_all(class_ = "midashigo")
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

    for n in range(0,len(number_list)):
        try:
            if descriptions[n].text:
                continue
        except:
            entries = n
            break
    try:
        for i in range (0,entries):
            print(titles[i].text + "\n")
            print(descriptions[i].text + "\n")
    except:
        return search_term +"という言葉は見つかれなかったです"
    return search_term + "という言葉はきっと面白いですね"