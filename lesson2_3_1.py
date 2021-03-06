import time
import math
from selenium import webdriver
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')

browser.get("http://suninjuly.github.io/alert_accept.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#x_element = browser.find_element_by_css_selector("[id='input_value']")
#x = x_element.text
#y = calc(x)

try:
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()