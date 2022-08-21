from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.weblio.jp/"
search_term = "木"



"""
Abre o driver do Chromium (instala se for necessário), 
passa o URL pra ele, 
procura a barra de pesquisa,
insere a palavra na caixa de pesquisa,
procura a palavra,
pega o url da página da palavra procurada,
fecha o driver.
"""

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(url)
search_bar = driver.find_element(By.NAME, "query")
search_bar.send_keys(search_term)
search_bar.send_keys(Keys.ENTER)
word_page_url = requests.get(driver.current_url)
driver.close()


#soup = BeautifulSoup(word_page_url.text, 'html.parser')
soup = BeautifulSoup(word_page_url.content, "html.parser")

print(soup.prettify())



#soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="mainContent")

#print(results.prettify())

#temperature_elements = results.find_all("div", class_="_flex _align-center _relative")

