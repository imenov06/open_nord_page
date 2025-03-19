import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
def count_nexign() -> int:
    driver.get("https://nexign.com/ru")
    page_text = driver.find_element("tag name", 'body').text
    count = len(re.findall(r'nexign', page_text, re.IGNORECASE))
    return count

if __name__ == '__main__':
    count = count_nexign()
    print(f"Количество вхождений 'nexign' на странице: {count}")
