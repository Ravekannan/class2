import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.select import Select


class uplod:
    global driver
    web = webdriver.ChromeOptions()
    abcd = {
        "download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\SeleniumProject\\Downloadfile\\"}
    web.add_experimental_option("prefs", abcd)
    web.add_argument("--start-maximized")
    web.add_argument("--incognito")
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe', options=web)
    #driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def upl(self):
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("(//div[@class='input-file-upload-hover-placeholder']//parent::div)[1]").click()
        pyperclip.copy("D:\\Besant\\JAVA\\Java basics.pdf")
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')
        print("uploaded sucessfully")



    def downdefaultlocation(self):
        driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
        driver.get("http://www.leafground.com/pages/download.html")
        driver.maximize_window()
        driver.find_element_by_link_text("Download Excel").click()
        time.sleep(5)

    def downspecificlocation(self):
        self.driver.get("http://www.leafground.com/pages/download.html")
        # self.driver.maximize_window()
        self.driver.find_element_by_link_text("Download Excel").click()


e =uplod()
#e.upl()
e.downspecificlocation()