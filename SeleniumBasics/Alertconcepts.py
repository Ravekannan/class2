import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class alertconcepts():
    global driver

    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/pages/Alert.html")
        alertbox = self.driver.find_element(by=By.XPATH, value="//button[text() = 'Alert Box']")
        alertbox.click()

        a=self.driver.switch_to.alert
        a.accept()
        time.sleep(2)

        confimbox = self.driver.find_element(by=By.XPATH, value="//button[text() = 'Confirm Box']")
        confimbox.click()
        confrimbox_obj = self.driver.switch_to.alert
        confrimbox_obj.dismiss()
        time.sleep(2)
        promptbox = self.driver.find_element(by=By.XPATH, value="//button[text() = 'Prompt Box']")
        promptbox.click()
        promptbox_obj = self.driver.switch_to.alert
        promptbox_obj.send_keys("besant technologies")
        promptbox_obj.accept()
        time.sleep(2)
        linebreak = self.driver.find_element(by=By.XPATH, value="//button[text() = 'Line Breaks?']")
        linebreak.click()
        linebreak_obj = self.driver.switch_to.alert
        print(linebreak_obj.text)
        linebreak_obj.accept()

obj=alertconcepts()
obj.launch()



