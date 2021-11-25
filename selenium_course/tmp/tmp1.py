# работа с выпадающими списками
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # для работы с выпадающими списками
import time
import math

try:
    ## функция для рассчета значения
    def calc(x,y):
        return str(x+y)


    x = 20
    y = 10
    z = calc(x,y)
    # заполняем все
    print(z)


    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

