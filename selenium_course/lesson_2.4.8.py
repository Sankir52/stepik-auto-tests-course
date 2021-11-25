# работа с ожиданиями
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    ## функция для рассчета значения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    #price = price.text
    #print(price)
    # ищем кнопку и жмем
    button = browser.find_element(By.XPATH, "//button[@id ='book']")
    button.click()


    x_element = browser.find_element(By.XPATH, "//span[@id ='input_value']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id ='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@id='solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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
