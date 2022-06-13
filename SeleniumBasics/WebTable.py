
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class webtab:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def table(self,actualtext,percentageval):
        self.driver.get("http://www.leafground.com/pages/table.html")
        totalrowvalue = self.driver.find_elements(by=By.XPATH, value="//section[@class='innerblock']//table//tbody//tr")
        sizeofrowlist = len(totalrowvalue)
        for x in range(2, sizeofrowlist+1):
            totalcolumnvalue = self.driver.find_elements(by=By.XPATH, value="//section[@class='innerblock']//table//tbody//tr[" + str(x) + "]//td")
            sizeofcolumnlist = len(totalcolumnvalue)
            text_Value = self.driver.find_element(by=By.XPATH, value="//section[@class='innerblock']//table//tbody//tr[" + str(x) + "]//td[1]").text
            print(text_Value)
            percentage_Value = self.driver.find_element(by=By.XPATH,
                                                  value="//section[@class='innerblock']//table//tbody//tr[" + str(
                                                      x) + "]//td[2]").text
            print(percentage_Value)
            if text_Value != actualtext and percentage_Value !=percentageval :
                self.driver.find_element(by=By.XPATH, value="//section[@class='innerblock']//table//tbody//tr[" + str(x) + "]//td[3]//input").click()
                #break
W= webtab()
W.table("Learn to interact with Elements","80%")