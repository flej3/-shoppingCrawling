import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
query = input("검색하고싶은 상품명을 입력해주세요: ")
serch_link = f"https://search.shopping.naver.com/search/all?query={query}"
driver.get(serch_link)
time.sleep(2)

producttitle = 
contentHeader = driver.find_element(By.CSS_SELECTOR, producttitle)
print("네이버 랭킹순으로 검색된 결과입니다.\n")
print(f"{}")


input()