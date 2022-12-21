from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)

    def get_info(self,query):
            self.query=query
            self.driver.get(url="https://www.wikipedia.org")
            search= self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)
            enter = self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button')
            enter.click()


