import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button2 = browser.find_element_by_css_selector("button.btn")
button2.click()

try:
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)

    button3 = browser.find_element_by_css_selector("[id='solve']")
    button3.click()

finally:
    time.sleep(10)
    browser.quit()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text