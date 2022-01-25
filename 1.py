from selenium import webdriver
import time
import math


def calc():
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_css_selector('[type = "submit"]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_el = browser.find_element_by_id("input_value")
    x = x_el.text
    y = calc()
    z = browser.find_element_by_id("answer")
    z.send_keys(y)
    button1 = browser.find_element_by_css_selector('[type = "submit"]')
    button1.click()


finally:
    time.sleep(10)
    browser.quit()