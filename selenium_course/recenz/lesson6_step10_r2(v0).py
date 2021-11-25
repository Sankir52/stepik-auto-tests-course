
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link)

# обов'язкові поля

# Заповнення поля "імя"
nameInput = browser.find_element_by_css_selector(".first_class [placeholder='Введите имя']")
nameInput.send_keys("Мария")

# Заповнення поля "Фамилия"
lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='Введите фамилию']")
lastnameInput.send_keys("Марьина")

# Заповнення поля "Email"
emailInput = browser.find_element_by_css_selector(".third_class [placeholder='Введите Email']")
emailInput.send_keys("maria@testmail.com")


button = browser.find_element_by_css_selector("button.btn")
button.click()

# Перевіляємо, що змогли зарегаться

time.sleep(1)

# знаходимо елемент де є текст
welcome_text_elt = browser.find_element_by_tag_name("h1")

# записуємо в змінну welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()