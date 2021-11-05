from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()
  browser.get(link)
  x_element = browser.find_element_by_css_selector("#input_value")
  x = x_element.text
  y = calc(x)
  z = browser.find_element_by_css_selector("#answer")
  z.send_keys(y)
  checkbox = browser.find_element_by_css_selector('[for = "robotCheckbox"]')
  checkbox.click()
  radiobutton = browser.find_element_by_css_selector('[for = "robotsRule"]')
  radiobutton.click()
  button = browser.find_element_by_css_selector('[type ="submit"]')
  button.click()
finally:
  time.sleep(5)
  browser.quit()

