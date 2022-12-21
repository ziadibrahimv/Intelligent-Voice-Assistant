from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/watch?v=TdrL3QxjyVw")
        search = self.driver.find_element(By.XPATH, '//*[@id="dismissable"]')
        video.click()


#assist=music()
#assist.play('dynamite by bts')