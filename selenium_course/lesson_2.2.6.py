# работа с выпадающими списками
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # для работы с выпадающими списками
import time
import math

try:
    ## функция для рассчета значения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # ищем элемент и его текст, получаем значение для функции
    x_element = browser.find_element(By.XPATH, "//span[@id ='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@id ='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    checkbos1 = browser.find_element(By.XPATH, "//input[@id ='robotCheckbox']") # чекбокс 1
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbos1)
    checkbos1.click()
    rbtn1 = browser.find_element(By.XPATH, "//input[@id ='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rbtn1)
    rbtn1.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
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
