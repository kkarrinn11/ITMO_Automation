from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements():
    driver = webdriver.Chrome()
    driver.get ('https://www.saucedemo.com/')


    elements = driver.find_elements (By.CSS_SELECTOR, '#user-name, #password, #login-button')
    if elements is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')

check_elements()

