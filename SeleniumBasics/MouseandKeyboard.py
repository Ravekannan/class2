from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class mouseandkeyboard():
    global driver

    def launch(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.leafground.com/pages/drop.html")
        self.driver.maximize_window()
    def mouseactions(self):
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(by=By.XPATH, value="(//a[text()='Electronics'])[2]")).perform()
        ac.move_to_element(self.driver.find_element(by=By.XPATH,value="//a[text()='Cameras and photos']")).click().perform()
    def fbmouseaction(self):
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(by=By.ID, value="email")).send_keys("sathishkumar").double_click().context_click().perform()
    def draganddropmouseactions(self):
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(by=By.ID, value="draggable")).drag_and_drop(self.driver.find_element(by=By.ID, value="draggable"),self.driver.find_element(by=By.ID, value="droppable")).perform()
    def mouseandkeyboard(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.facebook.com")
        self.driver.maximize_window()
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(by=By.ID, value="email"))\
            .send_keys("kumar.sathish189@gmail.com").key_down(Keys.TAB).key_up(Keys.TAB)\
            .move_to_element(self.driver.find_element(by=By.ID, value="pass"))\
            .send_keys("kumar.sathish189@gmail.com").key_down(Keys.TAB).key_up(Keys.TAB)\
            .key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
obj=mouseandkeyboard()
#obj.launch()
#obj.draganddropmouseactions()
obj.mouseandkeyboard()