import requests
from bs4 import BeautifulSoup
from .voice import * 

def get_word_dic (voice):
    voice.voice_answer("検索したい言葉を教えてください: ")
    search_term = input("\n自分:\n")
    url = "https://www.weblio.jp/content/" + search_term


    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    titles = soup.find_all(class_ = "midashigo")
    descriptions = soup.find_all(class_ = "Sgkdj")

    try:
        n = 0
        for description in descriptions:
            n = n + 1
        if n == 0:
           descriptions = soup.find_all(class_ = "Jtnhj")
           for description in descriptions:
                n = n + 1
    except:
        return search_term +"という言葉は見つかれなかったです"
    

    try:
        for i in range (0,n):
            print(titles[i].text + "\n")
            print(descriptions[i].text + "\n")
    except:
        return search_term +"という言葉は見つかれなかったです"
    return search_term + "という言葉はきっと面白いですね"