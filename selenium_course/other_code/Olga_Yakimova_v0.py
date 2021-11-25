from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://yandex.ru/internet")

start_btn = driver.find_element_by_class_name("button2_hovered_yes")
start_again_btn.click()

start_again_btn = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "measurement-management__start-again-button")))
start_again_btn.click()

# Получение значения из результатов "Входящие соединения"
speed_progress_bar = driver.find_element_by_css_selector(".measurement__load-box .load-box__row:first-child .measurement__progress-row .speed-progress-bar__left .speed-progress-bar__detailed")
speed_value = speed_progress_bar.text

# Не смогла получить числовое значение 4.51 из текста "4.51 Мбит/с"
if speed_value < 4.51
    print("Неуспешный результат")
else:
    print("Успешный результат." + "Скорость интернета: " + str(speed_value))

driver.quit()