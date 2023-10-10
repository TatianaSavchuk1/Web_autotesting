from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
        LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
        LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
        LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
        LOCATOR_ERR_LOCATOR = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
        LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
        LOCATOR_NAME_INPUT = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
        LOCATOR_EMAIL_INPUT = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
        LOCATOR_CONTENT_INPUT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
        LOCATOR_CONFIRM_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")

class OperationsHelper(BasePage):

    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)


    def enter_pass(self, word):
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)


    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BUTTON).click()


    def get_error_text(self):
        err_field = self.find_element(TestSearchLocators.LOCATOR_ERR_LOCATOR, time=3)
        return err_field.text


    def click_contact_btn(self):
        self.find_element((TestSearchLocators.LOCATOR_CONTACT_BTN)).click()


    def enter_name(self, name):
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_INPUT)
        name_field.clear()
        name_field.send_keys(name)


    def enter_email(self, email):
        name_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_INPUT)
        name_field.clear()
        name_field.send_keys(email)


    def enter_content(self, content):
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_INPUT)
        content_field.clear()
        content_field.send_keys(content)


    def click_confirm_btn(self):
        self.find_element((TestSearchLocators.LOCATOR_CONFIRM_BTN)).click()


    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text