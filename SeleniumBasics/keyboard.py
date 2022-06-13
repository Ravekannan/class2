import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class keyboardfuncation():

    def facebook(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://en-gb.facebook.com/")
        usrnamr = self.driver.find_element(by=By.ID,value="email")
        ac = ActionChains(self.driver)
        ac.move_to_element(usrnamr).send_keys("kumar.sathish189@gmail.com").perform()
        pyautogui.hotkey('ctrl', 'a')
        ac.context_click().perform()
        pyautogui.press(['down', 'down', 'down'])
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
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

    """ time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)"""

obj= keyboardfuncation()
obj.facebook()
