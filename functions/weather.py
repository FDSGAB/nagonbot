from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("headless")
        driver = webdriver.Chrome(options = options, executable_path=ChromeDriverManager().install())
        driver.get("https://www.climatempo.com.br/")
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.close()


        #Internet scrapping
        results = soup.find("span", id = "current-weather-temperature")

        if results.text == "":
            return "気温が取れなかったです。すみません。"
        
        return "今、気温は" + results.text + "です"
    except:
        return "すみません。いまインターネットがなそうです。"

