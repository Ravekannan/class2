import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class Firstclass():

    global driver
    def launch(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.facebook.com")
        """driver.maximize_window();
        driver.get("http://www.gmail.com")
        driver.back()
        driver.forward()
        driver.refresh()
        #driver.minimize_window();
        driver.set_window_size(200,300)"""
        time.sleep(2)
        #driver.find_element_by_id().send_keys()

    def login(self):

        self.driver.find_element(by=By.ID, value="email").send_keys("kumar")
        self.driver.find_element(by=By.NAME, value="pass").send_keys("test")
        self.driver.find_element(by=By.NAME, value="login").click()

obj=Firstclass()
obj.launch()
obj.login()