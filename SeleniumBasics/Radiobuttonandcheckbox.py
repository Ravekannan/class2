from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class radioandcheck():
    global driver



    def radioandcheckbox(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/home.html")
        self.driver.maximize_window()
        #Vealidation commands
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.find_element(by=By.XPATH, value="//*[text() = 'Radio Button']//parent::a").click()
        print(self.driver.find_element(by=By.ID, value="yes").is_selected()) #return the boolean value
        print(self.driver.find_element(by=By.ID, value="yes").is_displayed()) #return the boolean value
        print(self.driver.find_element(by=By.ID, value="yes").is_enabled()) #return the boolean value
        self.driver.find_element(by=By.ID , value="yes").click()
        self.driver.find_element(by=By.XPATH , value="(//*[@value='0'])[2]").click()
        print(self.driver.find_element(by=By.ID, value="yes").is_selected())  # return the boolean value
        print(self.driver.find_element(by=By.ID, value="yes").is_displayed())  # return the boolean value
        print(self.driver.find_element(by=By.ID, value="yes").is_enabled())# return the boolean value
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.find_element(by=By.ID, value="yes").get_attribute("class"))
        print(self.driver.find_element(by=By.ID, value="yes").get_attribute("type"))
        print(self.driver.find_element(by=By.ID, value="yes").text)
        print(self.driver.current_window_handle)




obj=radioandcheck()
obj.radioandcheckbox()
