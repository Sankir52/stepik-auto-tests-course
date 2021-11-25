# работа с выпадающими списками
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os  #для работы с ОС и файлами
try:
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'tmp1.py')  # добавляем к этому пути имя файла
    #element.send_keys(file_path)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(current_dir)
    print(file_path)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    #browser.quit()

