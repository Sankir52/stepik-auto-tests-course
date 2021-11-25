from selenium import webdriver
import time
try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath('//input[@placeholder= "Input your first name"]')
    input1.send_keys('Roman')
    input2 = browser.find_element_by_css_selector('input.form-control.second')
    input2.send_keys('Balu')
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys('balu@mail.ru')
    time.sleep(1)
    button = browser.find_element_by_css_selector('button.btn').click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()