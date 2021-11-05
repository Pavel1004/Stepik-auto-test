from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Pavel")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Pavlov")
    email = browser.find_element_by_name("email")
    email.send_keys("pavlov@mail.ru")
    filebutton = browser.find_element_by_css_selector("[type = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Stepik.txt')
    filebutton.send_keys(file_path)
    button = browser.find_element_by_css_selector('[type = "submit"]')
    button.click()

finally:
  time.sleep(5)
  browser.quit()
