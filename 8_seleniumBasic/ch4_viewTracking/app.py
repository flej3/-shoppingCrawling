import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
query = "python flask"
serch_link = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}"
driver.get(serch_link)
time.sleep(2)

target_blog_link = "https://cafe.naver.com/kstartupleaders/30396?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6ImtzdGFydHVwbGVhZGVycyIsImFydGljbGVJZCI6MzAzOTYsImlzc3VlZEF0IjoxNzA2Mzc1OTUwNjk2fQ.y5nANM0aWfeWpK0L-S7Nbbl3OzDKg27C2A-bD0Vx8jw"
link_selector = f'a[href^="{target_blog_link}"]'

BLOG_FOUND = False
for _ in range(7):
    try:
        element = driver.find_element(By.CSS_SELECTOR, link_selector)
        while True:
            new_element = element.find_element(By.XPATH, "./..")
            curRank = new_element.get_attribute("data-cr-rank")
            if curRank != None:
                print("현재랭크 : " , curRank)
                BLOG_FOUND = True
                break
            print("현재랭크 못찾음.")
            element = new_element
        if BLOG_FOUND:
            break
    except:
        print("타켓 블로그를 못찾음 -> 스크롤하겠습니다.")
        driver.execute_script("window.scrollBy(0,10000);")
        time.sleep(3)

print(f"{query}: 타켓 블로그의 랭크를 찾았습니다.")
print(f"{query}의 랭크는 : {curRank} 입니다.")

input()