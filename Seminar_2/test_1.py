
# Добавить в наш тестовый проект шаг добавления поста после входа. 
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.

import yaml
from module import Site



with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])


css_selector = 'span.mdc-text-field__ripple'
xpath = '//*[@id="login"]/div[3]/button/div'


print (site.get_element_property('css', css_selector, 'height'))
print (site.get_element_property('xpath', xpath, 'color'))


def test_step_1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input_1 = site.find_element('xpath', x_selector1)
    input_1.send_keys('test')
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input_2 = site.find_element('xpath', x_selector2)
    input_2.send_keys('test')
    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element('xpath', x_selector3)
    assert err_label.text == '401'

# test_step_1()


def test_step_3():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input_1 = site.find_element('xpath', x_selector1)
    input_1.send_keys(testdata['post_login'])
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input_2 = site.find_element('xpath', x_selector2)
    input_2.send_keys(testdata['post_pass'])
    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    btn.click()

    btn_selector2 = """//*[@id="create-btn"]"""
    btn3 = site.find_element('xpath', btn_selector2)
    btn3.click()

    x_selector3 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input_3 = site.find_element('xpath', x_selector3)
    input_3.send_keys('test post 1')

    btn_selector4 = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    btn4 = site.find_element('xpath', btn_selector4)
    btn4.click()

    btn_selector5 = """//*[@id="app"]/main/div/div[1]/div/div[1]/div[1]/button[1]"""
    btn5 = site.find_element('xpath', btn_selector5)
    btn5.click()

    test_selector = """//*[@id="app"]/main/div/div[1]/h1"""
    test_s = site.find_element('xpath', test_selector)
    assert test_s.text == 'test post 1'


test_step_3()