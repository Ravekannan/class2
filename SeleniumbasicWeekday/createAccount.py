import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class creataccount():
    global driver

    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.facebook.com")
        self.driver.maximize_window()
        createaccountbutton = self.driver.find_element(by=By.XPATH,
                                                       value="//*[@data-testid='open-registration-form-button']")
        createaccountbutton.click()
        # python wait

        # implicit wait
        self.driver.implicitly_wait(20)
        #time.sleep(5)
        firstname = self.driver.find_element(by=By.NAME, value="firstname")
        firstname.send_keys("sathish kumar")
        surname = self.driver.find_element(by=By.NAME, value="lastname")
        surname.send_keys("sathish")
        emailid = self.driver.find_element(by=By.NAME, value="reg_email__")
        emailid.send_keys("kumar.sathish189@gmail.com")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "reg_email_confirmation__")))
        reenteremailid = self.driver.find_element(by=By.NAME, value="reg_email_confirmation__")
        reenteremailid.send_keys("kumar.sathish189@gmail.com")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "reg_passwd__")))
        reenteremailid = self.driver.find_element(by=By.NAME, value="reg_passwd__")
        reenteremailid.send_keys("pswrd")
        daydropdown = self.driver.find_element(by=By.ID, value="day")
        deayselect=Select(daydropdown)
        deayselect.select_by_index(9)
        time.sleep(2)
        mondropdown = self.driver.find_element(by=By.ID, value="month")
        monselect = Select(mondropdown)
        monselect.select_by_value("9")
        time.sleep(2)
        yrdropdown = self.driver.find_element(by=By.ID, value="year")
        myrselect = Select(yrdropdown)
        myrselect.select_by_visible_text("2010")

    def multiselect(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/pages/Dropdown.html")
        self.driver.maximize_window()
        multidropdown = self.driver.find_element(by=By.XPATH, value="(//div[@class='example'])[6]//child::select")
        multiselect = Select(multidropdown)
        if(multiselect.is_multiple==True):
            multiselect.select_by_value("1")
            multiselect.select_by_index(3)
            multiselect.select_by_visible_text("Loadrunner")
            time.sleep(2)
            multiselect.deselect_by_index(3)
            time.sleep(2)
            multiselect.deselect_all()




obj= creataccount()
obj.multiselect()