from functions.function_tools import Browser
from bs4 import BeautifulSoup
import time
import os
import logging


def get_weather () -> str:

    os.environ['WDM_LOG'] = "false"
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    
    try: 
        chrome = Browser()
        chrome.driver.get("https://www.climatempo.com.br/")
        time.sleep(5)
        soup = BeautifulSoup(chrome.driver.page_source, "html.parser")
        chrome.driver.close()


        #Internet scrapping
        temperature = soup.find("span", id = "current-weather-temperature")
        condition = soup.find("span", id = "current-weather-condition")
        condition_text = translate_weather_condition(condition.text)
        if condition_text == "":
            condition_text = "わからないんです。"
        if temperature.text == "":
            return "気温が取れなかったです。すみません。"
        
        return "今、気温は" + temperature.text + "です。\n天気が" + condition_text
    except:
        return "すみません。いまインターネットはなさそうです。"
    

def translate_weather_condition(current_condition : str) -> str:
    
    condition_dictionary = {
                            'Chuva fraca':'弱い雨が降っています',
                            'Nuvens esparsas': '少し曇っています',
                            'Muitas nuvens' : 'すごく曇っています',
                            'Pancada de chuva':'降雨です',
                            'Trovoada':'雷雨です',
                            'Alguma nebulosidade' : 'なかなか曇っています'
                            }
    try:
        result = condition_dictionary[current_condition]
    except:
        result = ""
    return result
