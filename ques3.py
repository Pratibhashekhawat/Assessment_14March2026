from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,"Register").click()

sleep(2)
driver.find_element(By.ID,"name").send_keys("Pratibha")
sleep(2)
driver.find_element(By.ID,"email").send_keys("pratibha@gmail.com")
sleep(2)
driver.find_element(By.ID,"password").send_keys("123")
sleep(2)
driver.find_element(By.ID,"mobile").send_keys("123")
sleep(2)
driver.quit()