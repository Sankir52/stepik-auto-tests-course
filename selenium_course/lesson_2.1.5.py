from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    ## функция для рассчета значения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #input1 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[1]/input")  # First name*  # css селектор: div.first_block div:nth-child(1) input
    #input2 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[2]/input")  # Last name*   # css селектор: div.first_block div:nth-child(2) input
    #input3 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[3]/input")  # Email*       # css селектор: div.first_block div:nth-child(3) input

    # ищем элемент и его текст, получаем значение для функции
    x_element = browser.find_element(By.XPATH, "//span[@id ='input_value']")
    x = x_element.text
    y = calc(x)
    # заполняем все
    input1 = browser.find_element(By.XPATH, "//input[@id ='answer']")
    input1.send_keys(y)
    checkbos1 = browser.find_element(By.XPATH, "//input[@id ='robotCheckbox']") # чекбокс 1
    checkbos1.click()
    rbtn1 = browser.find_element(By.XPATH, "//input[@id ='robotsRule']")
    rbtn1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[contains(@class, 'btn')]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	#№ пока не понятно зачем, видимо дальше расскажут :)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
