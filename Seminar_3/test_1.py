from testpage import OperationsHelper
import yaml
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# def test_step_1(browser):
#
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login('test')
#     testpage.enter_pass('test')
#     testpage.click_login_button()
#     assert testpage.get_error_text() == '401'

#Добавить в проект тест по проверке механики работы формы
# Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.

def test_step_2(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['post_login'])
    testpage.enter_pass(testdata['post_pass'])
    testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.enter_name('test name')
    testpage.enter_email('test@email.com')
    testpage.enter_content('test content')
    testpage.click_confirm_btn()
    time.sleep(5)
    assert testpage.switch_to_alert() == 'Form successfully submitted'
