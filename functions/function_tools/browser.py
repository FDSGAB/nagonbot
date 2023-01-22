from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os


class browser:

    def __init__(self):
        os.environ['WDM_LOG'] = "false" 
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("headless")
        self.driver = webdriver.Chrome(options = options, executable_path=ChromeDriverManager().install())


    def __repr__(self):
        return "Chrome browser that connects to the internet in the background and does not display messages in the console"