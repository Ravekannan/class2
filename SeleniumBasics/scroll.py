from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class scrollvalidation():

    def launch(self):
        # shutil.rmtree(path)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/home.html")
    def scroll(self):
        self.driver.maximize_window()
        #scroll down
        self.driver.execute_script("window.scrollTo(0, 500)","")
        obj.screenshot("testcase1")
        time.sleep(1)
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -600)", 0)
        time.sleep(1)
        obj.screenshot("testcase2")
        # scroll right
        self.driver.execute_script("window.scrollTo(600, 0)", 0)
        time.sleep(1)
        obj.screenshot("testcase3")
        # scroll left
        self.driver.execute_script("window.scrollTo(-600, 0)", 0)

        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        obj.screenshot("testcase4")
        # scroll top vertical
        self.driver.execute_script("window.scrollTo(0, 0)","")
        # screenshot
        obj.screenshot("testcase5")

        # scroll to a specific element
        element=self.driver.find_element(by=By.XPATH,value="//h5[text()='Down Files']//parent::a")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        obj.screenshot("testcase6")
        element.click()
        obj.screenshot("testcase7")

        CUR_DIR = os.path.abspath(os.curdir)
        print(CUR_DIR)
        ROOT_DIR = os.path.abspath(os.pardir)
        print(ROOT_DIR)
        #screenshot
       # root_path=os.path.dirname("\\screenshot\\image.png")
        #root_path = os.path.dirname(os.path.abspath("image.png"))
        #ROOT_DIR = os.path.abspath(os.curdir)

        #print(root_path)
        #print(ROOT_DIR)


    def screenshot(self,filename):
        ROOT_DIR = os.path.abspath(os.pardir)
        self.driver.save_screenshot(
            ROOT_DIR+"\\screenshot\\"+filename+".png")

obj=scrollvalidation()
obj.launch()
obj.scroll()