from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
#options.headless = True
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get("https://techwithtim.net/")
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()