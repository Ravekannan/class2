import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class frame:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def FRMH(self):
        self.driver.get("http://www.leafground.com/pages/frame.html")
        self.driver.maximize_window()
        #self.driver.find_element_by_id("Click").click()
        frame_to = self.driver.find_elements(by=By.TAG_NAME,value="iframe")
        frame_count = len(frame_to)
        #print(frame_count)
        for sat in range(0,frame_count):
            self.driver.switch_to.frame(sat) # switch over in to Frame
            value = self.driver.find_elements(by=By.ID,value="Click")
            elemetnsize= len(value)
            if elemetnsize>0:
                self.driver.find_element_by_id("Click").click()
                break
            self.driver.switch_to.default_content() # switch back from the Frame

    def FRMHinsideFRMH(self):
        identified ="not done"
        self.driver.get("http://www.leafground.com/pages/frame.html")
        self.driver.maximize_window()

        # self.driver.find_element_by_id("Click").click()
        frame_to = self.driver.find_elements(by=By.TAG_NAME,value="iframe")
        frame_count = len(frame_to)
        print(frame_count)
        for X in range(0, frame_count):
            self.driver.switch_to.frame(X)
            frame_inner = self.driver.find_elements(by=By.TAG_NAME,value="iframe")
            frame_inner_count = len(frame_inner)
            print(frame_inner_count)
            if frame_inner_count>0:
                for Y in range(0, frame_inner_count):
                    self.driver.switch_to.frame("frame2")
                    value = self.driver.find_elements(by=By.ID,value="Click1")
                    elemetnsize = len(value)
                    if elemetnsize > 0:
                        self.driver.find_element_by_id("Click1").click()
                        identified = "done"
                        break
                    else:
                        self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.default_content()
            if identified == "done":
               break


F= frame()
#F.FRMH()
F.FRMHinsideFRMH()