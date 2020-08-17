import math
import time
from selenium import webdriver

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')

browser.get("http://suninjuly.github.io/math.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)

try:
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
