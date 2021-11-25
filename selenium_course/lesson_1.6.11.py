from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #выбор страницы для проверки, закомментировать не нужную!
    link = "http://suninjuly.github.io/registration1.html"  # Рабочий вариант
    #link = "http://suninjuly.github.io/registration2.html"  # Заведомо не рабочий вариант
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ## Два варианта поиска полей, раскомментируйте нужный
    ### вариант поиска через placeholder, не красиво но просто
    #input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")  # First name*
    #input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")  # Last name*
    #input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")  # Email*

    ### вариант поиска по структуре. Сложнее, но надежнее, верстка меняется реже подписей, правда не в нашем случае ^_^
    input1 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[1]/input")  # First name*  # css селектор: div.first_block div:nth-child(1) input
    input2 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[2]/input")  # Last name*   # css селектор: div.first_block div:nth-child(2) input
    input3 = browser.find_element(By.XPATH, "//div[@class ='first_block']/div[3]/input")  # Email*       # css селектор: div.first_block div:nth-child(3) input

    # заполняем найденные поля
    input1.send_keys("Иван")
    input2.send_keys("Петров")
    input3.send_keys("ПОЧТА@ПОЧТА")
    # смотрим что заполнилось
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[contains(@class, 'btn')]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	#№ пока не понятно зачем, видимо дальше расскажут :)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
