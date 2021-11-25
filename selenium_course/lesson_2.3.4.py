# работа с алертами
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    ## функция для рассчета значения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем кнопку и жмем
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
    button.click()

    # Ищем алерт
    confirm  = browser.switch_to.alert
    confirm .accept()
    time.sleep(2)
    # ищем элемент и его текст, получаем значение для функции
    x_element = browser.find_element(By.XPATH, "//span[@id ='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id ='answer']")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
    button.click()

    # ждем загрузки страницы
    time.sleep(2)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	#№ пока не понятно зачем, видимо дальше расскажут :)
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
