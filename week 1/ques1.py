from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com")

driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#_R_1h6kqsqppb6amH1_").send_keys("pratibha@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#_R_1hmkqsqppb6amH1_").send_keys('pratibha@123')
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()
sleep(2)
driver.quit()