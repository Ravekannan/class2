import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class verificationandvalidation():
    global driver

    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.makemytrip.com/")
    def verification(self):
        self.driver.get("http://www.leafground.com/pages/Edit.html")
        #Get Title
        print(self.driver.title)
        # Get currenturl
        print(self.driver.current_url)
        # Get attribute
        classattributename = self.driver.find_element(by=By.ID,value="email").get_attribute("style")
        print(classattributename)
        # Get text
        textoftheelement = self.driver.find_element_by_xpath("(//label[@for='email'])[1]").text
        print(textoftheelement)

        # currentwindowname
        classattributename = self.driver.current_window_handle
        print(classattributename)
        classattributenames = self.driver.window_handles
        print(classattributenames)
    def validation(self):
        self.driver.get("http://www.leafground.com/pages/checkbox.html")
        time.sleep(2)
        print(self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_displayed())
        print(self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_enabled())
        valu= self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_selected()
        print(valu)
        if valu == False :
            self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").click()
        print(self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_selected())
        print(self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_displayed())
        print(self.driver.find_element(by=By.XPATH,value="(//input[@type='checkbox'])[1]").is_enabled())

verval= verificationandvalidation()
verval.launch()
verval.validation()
