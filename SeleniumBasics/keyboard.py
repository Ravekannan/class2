import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class keyboardfuncation():

    def facebook(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://en-gb.facebook.com/")
        usrnamr = self.driver.find_element_by_id("email")
        ac = ActionChains(self.driver)
        ac.move_to_element(usrnamr).send_keys("sathish").double_click().context_click().perform()
        #pyautogui.press(['down', 'down', 'down'])
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('enter')
        # time.sleep(10)
        # ac.key_down('tab')
        # ac.key_up('tab')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'v')

    """ time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)"""

obj= keyboardfuncation()
obj.facebook()
