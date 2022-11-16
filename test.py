# Установите Selenium в терминале: pip install selenium
# либо просто в коде нажмите на подчеркнутые ошибки и на установить selenium оно само стянет все и установит
# Скачайте вебдрайвер и добавьте его в переменную среды Path как на уроке говорил Любомир
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua")
driver.maximize_window()
time.sleep(5)

# quit from browser
driver.quit()
