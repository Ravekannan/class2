import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class multiselect():

    global driver
    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/pages/Dropdown.html")
        multiselect1=self.driver.find_element(by=By.XPATH,value="(//div[@class='example']//select)[6]")
        selectclass=Select(multiselect1)
        print(selectclass.is_multiple)
        if(selectclass.is_multiple==True):
            selectclass.select_by_value("1")
            time.sleep(1)
            selectclass.select_by_index(2)
            time.sleep(1)
            selectclass.select_by_visible_text("UFT/QTP")
            time.sleep(1)
            selectclass.deselect_by_index(2)
            time.sleep(1)
            selectclass.deselect_all()


obj=multiselect()
obj.launch()
