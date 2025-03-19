import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def open_nexign_nord_page():
    driver.get("https://nexign.com/ru")
    time.sleep(1)
    try:
        driver.find_element("xpath", "//button[@class='header__burger']").click()
        time.sleep(1)
    except:
        print("Меню-бургер не требуется")
    finally:
        driver.find_element("xpath", "//li[./span[contains(text(), 'Продукты и решения')]]").click()
        time.sleep(1)
        driver.find_element("xpath", "//li[./span[contains(text(), 'Инструменты для ИТ-команд')]]").click()
        time.sleep(1)
        driver.find_element("xpath", "//li[@class='menu-item']/a[text()='Nexign Nord']").click()
        time.sleep(3)


if __name__ == '__main__':
    open_nexign_nord_page()