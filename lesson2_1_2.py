import math
import time
from selenium import webdriver

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')

browser.get("http://suninjuly.github.io/get_attribute.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
ln(abs(12*sin(x)))

x_element = browser.find_element_by_css_selector("img#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

try:
    input1 = browser.find_element_by_css_selector("input#answer")
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
