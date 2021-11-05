from selenium import webdriver
import time
import math
def calc():
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button1 = browser.find_element_by_css_selector('[type = "submit"]')
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc()
    z = browser.find_element_by_id("answer")
    z.send_keys(y)
    button = browser.find_element_by_css_selector('[type = "submit"]')
    button.click()

finally:
  time.sleep(5)
  browser.quit()