# unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"  # Рабочий вариант
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[1]/input")  # First name*  # css селектор: div.first_block div:nth-child(1) input
        input2 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[2]/input")  # Last name*   # css селектор: div.first_block div:nth-child(2) input
        input3 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[3]/input")  # Email*       # css селектор: div.first_block div:nth-child(3) input
        # заполняем найденные поля
        input1.send_keys("Иван")
        input2.send_keys("Петров")
        input3.send_keys("ПОЧТА@ПОЧТА")
        # смотрим что заполнилось
        #time.sleep(2)
        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH ,"//button[contains(@class, 'btn')]")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Тест провален")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"  # Рабочий вариант
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[1]/input")  # First name*  # css селектор: div.first_block div:nth-child(1) input
        input2 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[2]/input")  # Last name*   # css селектор: div.first_block div:nth-child(2) input
        input3 = browser.find_element(By.XPATH,
                                      "//div[@class ='first_block']/div[3]/input")  # Email*       # css селектор: div.first_block div:nth-child(3) input
        # заполняем найденные поля
        input1.send_keys("Иван")
        input2.send_keys("Петров")
        input3.send_keys("ПОЧТА@ПОЧТА")
        # смотрим что заполнилось
        # time.sleep(2)
        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Тест провален")


if __name__ == "__main__":
    unittest.main()