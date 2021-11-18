from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

        firstname = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        firstname.send_keys("Pavel")
        lastname = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        lastname.send_keys("Pavlov")
        email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        email.send_keys("pavlov@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_registration2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        firstname = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        firstname.send_keys("Pavel")
        lastname = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        lastname.send_keys("Pavlov")
        email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        email.send_keys("pavlov@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()



