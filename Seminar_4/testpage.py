import logging
from selenium.webdriver.common.by import By
from BaseApp import BasePage
import yaml

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#Adding sending test results via e-mail

fromaddr = "redtitania2045@mail.ru"
toaddr = "redtitania2045@gmail.com"
mypass = "2jd5iVHbMMnEnKCXf84F"
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hello from python"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

body = "This is a testing message"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

class TestSearchLocators:

    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception during operation with {locator}')
            return False
        return True


    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True


    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'The text {text} was found in field {field}')
        return text


#ENTER TEXT

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')


    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password')


    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME_INPUT'], word, description='name')


    def enter_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL_INPUT'], email, description='email')


    def enter_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_INPUT'], content, description='content')


#SWITCH TO ALERT

    def switch_to_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None


#CLICK BUTTON

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BUTTON'], description='login')


    def click_contact_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact')


    def click_confirm_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONFIRM_BTN'], description='confirm')


#GET TEXT

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERR_LOCATOR'])