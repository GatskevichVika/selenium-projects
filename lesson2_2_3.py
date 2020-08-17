import os
import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')

browser.get("http://suninjuly.github.io/file_input.html")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'C:\\Users\\Vika\\Desktop\\UItest\\file.txt')

try:

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("test@test.ru")
    input4 = browser.find_element_by_css_selector("[type='file']")
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
