import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


class firstclass():

    def launch(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #browser = webdriver.Edge(executable_path=r'D:\\Software\\edgedriver_win64\\msedgedriver.exe')

        browser.maximize_window()
        #browser.minimize_window()
        browser.get("https://www.facebook.com/")
        #username=browser.find_element_by_id("email")
        username=browser.find_element(by=By.ID , value="email")
        username.send_keys("kumar.sathish189@gmail.com")
        time.sleep(2)
        #username.clear()
        username1 = browser.find_element(by=By.NAME, value="pass")
        username1.send_keys("sathish1990")
        time.sleep(2)
        forgotpassword=browser.find_element(by=By.LINK_TEXT , value="Forgotten password?")
        forgotpassword.click()
        time.sleep(2)
        #emailid = browser.find_element(by=By.CSS_SELECTOR, value="input#identify_email")
        #emailid = browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _9o1w[name=email]")
        #emailid = browser.find_element(by=By.CSS_SELECTOR, value="input[name=email]")
        emailid = browser.find_element(by=By.XPATH, value="//input[@id='identify_email']")
        emailid.send_keys("kumar.sathish189@gmailcom")
        time.sleep(4)
        loginbutton = browser.find_element(by=By.XPATH, value="(//span[text() = 'Log In'])[2]")
        loginbutton.click()


obj=firstclass()
obj.launch()
