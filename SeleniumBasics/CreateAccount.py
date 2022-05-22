import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CreateAccount():

    global driver
    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.facebook.com")
        self.driver.maximize_window()
        createaccountbutton=self.driver.find_element(by=By.XPATH,value="//*[@data-testid='open-registration-form-button']")
        createaccountbutton.click()
        # python wait
        #time.sleep(2)
        #implicit wait
        self.driver.implicitly_wait(20)
        firstname = self.driver.find_element(by=By.NAME,value="firstname")
        firstname.send_keys("sathish kumar")
        surname = self.driver.find_element(by=By.NAME, value="lastname")
        surname.send_keys("sathish")
        emailid = self.driver.find_element(by=By.NAME, value="reg_email__")
        emailid.send_keys("kumar.sathish189@gmail.com")
        #explicit wait
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "reg_email_confirmation__")))
        reenteremailid = self.driver.find_element(by=By.NAME, value="reg_email_confirmation__")
        reenteremailid.send_keys("kumar.sathish189@gmail.com")

        date=self.driver.find_element(by=By.ID, value="day")

        month = self.driver.find_element(by=By.ID, value="month")
        year = self.driver.find_element(by=By.ID, value="year")
        datedropdownobj=Select(date)
        dateismultipleornot=datedropdownobj.is_multiple
        print(dateismultipleornot)
        datedropdownobj.select_by_index(8)
        monthdropdownobj = Select(month)
        monthdropdownobj.select_by_visible_text("Sep")
        yeardropdownobj = Select(year)
        yeardropdownobj.select_by_value("2000")




        signin = self.driver.find_element(by=By.XPATH, value="(// button[text() = 'Sign Up'])[1]")
        signin.click()




obj=CreateAccount()
obj.launch()
