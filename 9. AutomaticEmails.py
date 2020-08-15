from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

x = 0

while x < 10:
    driver = webdriver.Firefox()
    driver.get('https://mail.google.com/mail/u/0/#inbox')

    driver.find_element_by_id('identifierId').send_keys('goncalomanuelreis@gmail.com')

    seguinteElem = driver.find_element_by_id('identifierNext')
    seguinteElem.click()

    passwordElem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, 'password')))
    passwordElem.send_keys('oXvlviIYdSafO6n5')

    passwordNext = driver.find_element_by_id('passwordNext')
    WebDriverWait(driver, 30).until_not(EC.visibility_of_element_located((By.XPATH, "//div[@class='ANuIbb IdAqtf']")))
    passwordNext.click()

    composeButton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@gh='cm']")))
    composeButton.click()

    to = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@name='to']")))
    to.send_keys('up200806872@fpce.up.pt')

    subject = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='subjectbox']")))
    subject.send_keys('Boa noite.')

    message = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
    message.send_keys('Aprendi a automatizar o envio de emails. Como prova, envio estes 10 emails, todos de forma automática. No futuro, quando estivermos em desacordo e como vingança, poderei enviar-te, a título de exemplo, mil.')

    ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
    time.sleep(3)
    driver.quit()

    x += 1






