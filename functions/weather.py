from .function_tools import *
from bs4 import BeautifulSoup
import time


def get_weather () -> str:
    """
    Abre o driver do Chromium (instala se for necessário), 
    passa o URL pra ele, 
    delay para a página carregar,
    pega o HTML da página da página procurada,
    fecha o driver.
    """
    try: 
        chrome = browser()
        chrome.driver.get("https://www.climatempo.com.br/")
        time.sleep(5)
        soup = BeautifulSoup(chrome.driver.page_source, "html.parser")
        chrome.driver.close()


        #Internet scrapping
        results = soup.find("span", id = "current-weather-temperature")
        if results.text == "":
            return "気温が取れなかったです。すみません。"
        
        return "今、気温は" + results.text + "です"
    except:
        return "すみません。いまインターネットがなそうです。"