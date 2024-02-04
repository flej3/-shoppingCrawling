from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
#1. 웹 브라우저 주소창을 컨트롤하기 driver.get()
# driver.get("https://www.naver.com")
# time.sleep(1)

# driver.get("https://google.com")
# time.sleep(2)

# driver.back()
# time.sleep(1)

# driver.forward()
# time.sleep(1)

# driver.refresh()
# time.sleep(1)
# print("End")

# input()

# 2. browser information
# 2-1. title, current_uri
# driver.get("https://www.naver.com")
# time.sleep(1)
# title = driver.title
# print(title, "가 타이틀이다.")

# curUrl = driver.current_url
# print(curUrl, "가 주소이다.")

# input()



# 2. Driver wait
# 2-1. title, current_uri
# driver.get("https://www.naver.com")

# try:
#     selector = "#feed > div.ContentHeaderView-module__content_header___nSgPg > div > ul > li:nth-child(3) > a"
#     # WebDriverWait(driver, 100).until(EC.presence_of_element_located(
#     #     By.CSS_SELECTOR, selector)
#     # )
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
#         By.CSS_SELECTOR, selector))
#         )
#     element.click()
# except:
#     print("예외 발생, 예외 처리 코드 실행하기")
# print("다음 코드 실행")

# input()

# 네이버 페이지로 이동
driver.get("https://www.naver.com")
selector = "#search-btn"
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    # 요소를 클릭하거나 다른 작업을 수행할 수 있습니다.
    element.click()
except Exception as e:
    contentHeader = driver.find_element(By.CSS_SELECTOR, selector)
    contentHeader.click()
    print("예외 발생, 예외 처리 코드 실행하기")

print("다음 코드 실행")

# 드라이버 종료
input()



# # 2-1. 요소를 찾아서 Copy해옴. 실제 웹 브라우저 + 개발자 도구
# css_selector = "#feed > div.ContentHeaderView-module__content_header___nSgPg > div > ul > li:nth-child(3) > a"

# # 2-2. 찾아온 요소를 find_element로 가져오기 -> 상자(변수)에 담기.
# contentHeader = driver.find_element(By.CSS_SELECTOR, css_selector)

# # 3-1. 데이터를 가져오기
# print(contentHeader.text)

# # 3-2. 요소를 클릭하기(액션)
# contentHeader.click()

# input()