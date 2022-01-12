from selenium import webdriver
import time
import math


def calc():
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link ="http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc()
    z = browser.find_element_by_id("answer")
    z.send_keys(y)
    button = browser.find_element_by_css_selector("[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button.click()

finally:
  time.sleep(5)
  browser.quit()


