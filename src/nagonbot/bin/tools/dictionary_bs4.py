import requests
from bs4 import BeautifulSoup
from .voice import * 

def get_word_dic () -> str:
    Voice().voice_answer("検索したい言葉を教えてください: ")
    search_term = input("\n自分:\n")
    url = "https://www.weblio.jp/content/" + search_term


    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    titles = soup.find_all(class_ = "midashigo")
    descriptions = soup.find_all(class_ = "Sgkdj")

    try:
        number_of_entries = len(descriptions)
        if number_of_entries == 0:
           descriptions = soup.find_all(class_ = "Jtnhj")
           number_of_entries = len(descriptions)
        if number_of_entries == 0:
            return search_term +"という言葉は見つかれなかったです"    
    except:
        return search_term +"という言葉は見つかれなかったです"
    

    try:
        for i in range (0, number_of_entries):
            print(titles[i].text + "\n")
            print(descriptions[i].text + "\n")
    except:
        return search_term +"という言葉は見つかれなかったです"
    return search_term + "という言葉はきっと面白いですね"