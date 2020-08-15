from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os, time

fp = webdriver.FirefoxProfile(r'C:\Users\Gonçalo\AppData\Roaming\Mozilla\Firefox\Profiles\m72n9x3n.default-release')
fp.set_preference("browser.download.dir", os.getcwd())
driver = webdriver.Firefox(firefox_profile=fp)
search_keywords = "Haechan"
driver.get(f'https://www.flickr.com/search/?text={search_keywords}')
elems = driver.find_elements_by_class_name('overlay')
for i in range(len(elems)):
    time.sleep(1.5)
    driver.find_element_by_xpath("(//a[@class='overlay'])[" + str(i + 1) + "]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[1]//div//div[2]//div//div[5]//div[3]//a"))).click()
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Quadrado > a:nth-child(1)"))).click()
        driver.back()
    except:        
        driver.back()
driver.quit()

