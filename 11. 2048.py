from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://gabrielecirulli.github.io/2048/')
htmlElem = driver.find_element_by_tag_name('html')
retryElem = driver.find_element_by_xpath("//a[@class='retry-button']")

while True:
    if retryElem.is_displayed() == False:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
    else:
        driver.find_element_by_xpath("//a[@class='retry-button']").click()
