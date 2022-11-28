import time

from Rozetka.pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://rozetka.com.ua/ua/")
    page.open()
    time.sleep(3)
