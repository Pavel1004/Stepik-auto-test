from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc():
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_id("book")
    button.click()
    x_el = browser.find_element_by_id("input_value")
    x = x_el.text
    y = calc()
    z = browser.find_element_by_id("answer")
    z.send_keys(y)
    button1 = browser.find_element_by_css_selector('[type ="submit"]')
    button1.click()

finally:
  time.sleep(15)
  browser.quit()
