import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')

browser.get("http://suninjuly.github.io/selects1.html")


def calc():
    z = str(int(x) + int(y))
    return z

x_element = browser.find_element_by_css_selector("span#num1.nowrap")
x = x_element.text
y_element = browser.find_element_by_css_selector("span#num2.nowrap")
y = y_element.text
z = calc()
try:
    print(z)
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value("z")  # ищем элемент с номером равным сумме

    select = Select( browser.find_element_by_css_selector("select#dropdown.custom-select"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
