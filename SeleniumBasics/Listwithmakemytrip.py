from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class makemytrip():
    global driver

    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.makemytrip.com/")

    def fromList(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='langCardClose']")))
        self.driver.find_element(by=By.XPATH, value="//span[@class='langCardClose']").click()
        FromWebelement = self.driver.find_element(by=By.XPATH, value="//label[@for='fromCity']")
        FromWebelement.click()

    def fromandTo(self,giventext):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='react-autosuggest__suggestions-list']//li[1]")))
        """"FromWebelementList = self.driver.find_elements(by=By.XPATH,
                                                           value="//label[@for='fromCity']//parent::div//ul//li")"""
        FromWebelementList = self.driver.find_elements(by=By.XPATH,
                                                       value="//ul[@class='react-autosuggest__suggestions-list']//li")
        listsize=len(FromWebelementList)
        print(listsize)
        for eachvalue in range(1,listsize+1):
           """ FromeachWebelementinList = self.driver.find_element(by=By.XPATH,
                                                           value="//label[@for='fromCity']//parent::div//ul//li["+str(eachvalue)+"]//div[contains(@class,'pushRight')]")"""
           FromeachWebelementinList = self.driver.find_element(by=By.XPATH,
                                                               value="//ul[@class='react-autosuggest__suggestions-list']//li[" + str(
                                                                   eachvalue) + "]//div[contains(@class,'pushRight')]")
           actualcountrytext=FromeachWebelementinList.text
           print(actualcountrytext)
           if (actualcountrytext==giventext):
                FromeachWebelementinList.click()
                break


obj=makemytrip()
obj.launch()
obj.fromList()
obj.fromandTo("PNQ")
obj.fromandTo("MAA")
