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

        #self.driver.find_element(by=By.ID, value="email").send_keys("kumar")
        #self.driver.find_element(by=By.CSS_SELECTOR, value="input#email").send_keys("kumar")
        #self.driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy[data-testid=royal_email]").send_keys("kumar")

        #self.driver.find_element(by=By.CSS_SELECTOR, value="input[data-testid=royal_email]").send_keys("kumar")
        self.driver.find_element(by=By.XPATH, value="//input[@data-testid='royal_email']").send_keys("kumar.sathish189@gmail.com")

        #self.driver.find_element(by=By.NAME, value="pass").send_keys("test")
        self.driver.find_element(by=By.XPATH, value="// input[contains( @class ,'_6luy') and @ name='pass']").send_keys(
            "kAdmin@123")

    
           #self.driver.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy").send_keys("test")
        #self.driver.find_element(by=By.LINK_TEXT, value="Forgotten password?").click()
        #self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="gotten").click()
        #self.driver.find_element(by=By.NAME, value="login").click()

obj=Firstclass()
obj.launch()
obj.login()