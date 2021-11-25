# работа с файлами
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os  #для работы с ОС и файлами
try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # ищем элемент и его текст, получаем значение для функции
    input1 = browser.find_element(By.XPATH, "//input[@name ='firstname']")
    input1.send_keys('123123')
    input2 = browser.find_element(By.XPATH, "//input[@name ='lastname']")
    input2.send_keys('qeqweqwe')
    input3 = browser.find_element(By.XPATH, "//input[@name ='email']")
    input3.send_keys('asdasdassd')

    input_f = browser.find_element(By.XPATH, "//input[@id ='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input_f.send_keys(file_path)

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
