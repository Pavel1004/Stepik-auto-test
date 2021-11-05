from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)
  sunduk = browser.find_element_by_id("treasure")
  treasure = sunduk.get_attribute("valuex")
  y = calc(treasure)
  z = browser.find_element_by_css_selector("#answer")
  z.send_keys(y)
  checkbox = browser.find_element_by_css_selector("#robotCheckbox")
  checkbox.click()
  radiobutton = browser.find_element_by_css_selector("#robotsRule")
  radiobutton.click()
  button = browser.find_element_by_css_selector('[type ="submit"]')
  button.click()
finally:
  time.sleep(5)
  browser.quit()