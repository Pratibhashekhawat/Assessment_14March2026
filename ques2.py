from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.youtube.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']").send_keys(" melody hits")
sleep(2)
driver.find_element(By.CSS_SELECTOR,'.ytSearchboxComponentSearchButton').click()
sleep(2)
driver.quit()