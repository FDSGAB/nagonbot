from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = "https://www.weblio.jp/"
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
search_term = "木"

driver.get(URL)
search_bar = driver.find_element(By.NAME, "query")
search_bar.send_keys(search_term)
search_bar.send_keys(Keys.ENTER)

while True:
    m = int(input())
    if m ==1:
        break

#Fecha o brouser
driver.close()


#soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="mainContent")

#print(results.prettify())

#temperature_elements = results.find_all("div", class_="_flex _align-center _relative")

