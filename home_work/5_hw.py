from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ('https://www.saucedemo.com/')


elements = driver.find_element (By.CSS_SELECTOR, '#user-name, #password, .submit-button')
if elements is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')



