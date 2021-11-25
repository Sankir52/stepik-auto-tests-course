# работа с выпадающими списками
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # для работы с выпадающими списками
import time
import math

try:
    ## функция для рассчета значения
    def calc(x,y):
        z = x+y
        return str(z)

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # ищем элемент и его текст, получаем значение для функции
    x_element = browser.find_element(By.XPATH, "//span[@id ='num1']")
    x = int(x_element.text)
    y_element = browser.find_element(By.XPATH, "//span[@id ='num2']")
    y = int(y_element.text)
    z = calc(x,y)
    print(z)
    # выбираем нужное из выпадающего списка
    select = Select(browser.find_element(By.XPATH, "//select[@id ='dropdown']")) # ищем список
    select.select_by_value(z)  # ищем значение
    #select.click() # при работе с либой Select клик по форме не надо. он сам выбирает
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
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
