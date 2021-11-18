import unittest
from selenium import webdriver


link1 = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link1)


class TestRegistration(unittest.TestCase):

    def test_firstname(self):
        firstname = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        firstname.send_keys("Pavel")
        self.assertEqual(firstname.get_attribute('placeholder'), 'Input your first name', "first_error")

    def test_lastname(self):
        lastname = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        lastname.send_keys("Pavlov")
        self.assertEqual(lastname.get_attribute('placeholder'), 'Input your last name', "last_error")

    def test_email(self):
        email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        email.send_keys("pavlov@mail.ru")
        self.assertEqual(email.get_attribute('placeholder'), 'Input your email', "email_error")

    def test_button(self):
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    def test_link1(self):
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Registration', "page_open_error")


if __name__ == '__main__':
    unittest.main()



