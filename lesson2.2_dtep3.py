from selenium import webdriver
import time
import math
def calc():
    return str(int(a) + int(b))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_element = browser.find_element_by_id("num1")
    b_element = browser.find_element_by_id("num2")
    a = a_element.text
    b = b_element.text
    z = calc()
    drop = browser.find_element_by_id("dropdown")
    drop.send_keys(z)
    button = browser.find_element_by_css_selector('[type ="submit"]')
    button.click()
finally:
  time.sleep(5)
  browser.quit()