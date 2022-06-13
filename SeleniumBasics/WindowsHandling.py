import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class winhandle:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def twowinhandle(self):
        self.driver.get("http://www.leafground.com/pages/Window.html")
        self.driver.maximize_window()
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_id("home").click()

        ALL_window = self.driver.window_handles

        for child in ALL_window :

            if child!=parent_window :
                self.driver.switch_to.window(child) # switch in to particular window
                self.driver.maximize_window()
                elementpreset = self.driver.find_elements(by=By.XPATH,value="//h5[text()='Edit']//parent::a") # eleent identification in the window
                elementpresent_count = len(elementpreset)
                if elementpresent_count >0 :
                    self.driver.find_element(by=By.XPATH,value="//h5[text()='Edit']//parent::a").click()
                    self.driver.find_element_by_id("email").send_keys("kumar.sathish189")
                    #self.driver.close()
                    self.driver.switch_to.window(parent_window)
                    self.driver.quit()

                    break

    def morethantwowinhandle(self):
        self.driver.get("http://www.leafground.com/pages/Window.html")
        self.driver.maximize_window()
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath("//button[text()='Open Multiple Windows']").click()

        ALL_window = self.driver.window_handles

        for child in ALL_window :

            if child!=parent_window :
                self.driver.switch_to.window(child)
                self.driver.maximize_window()
                elementpreset = self.driver.find_elements_by_id("home")
                elementpresent_count = len(elementpreset)
                if elementpresent_count >0 :
                    self.driver.find_element_by_id("home").click()
                    self.driver.find_element_by_xpath("//h5[text()='Edit']//parent::a").click()
                    self.driver.find_element_by_id("email").send_keys("kumar.sathish189")
                    #self.driver.switch_to.window(parent_window)
                    #self.driver.quit()
                    break

                else  :
                    print()
                     #self.driver.switch_to.window(parent_window)

W= winhandle()
W.twowinhandle()