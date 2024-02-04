import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

#스크롤
def infinite_scroll(driver):
    before_h = driver.execute_script("return window.scrollY")

    while True:
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(1)
        after_h = driver.execute_script("return window.scrollY")
        if before_h == after_h:
            break
        before_h = after_h
    time.sleep(5)

#상품 검색
def search_product (driver):
    query = input("검색어: ")
    driver.get(f"https://search.shopping.naver.com/search/all?query={query}")
    driver.implicitly_wait(10)

#상품명, 가격 출력
def print_ad_product(items, name_selector, price_selector):
    for item in items:
        try:
            product_name = item.find_element(By.CSS_SELECTOR, name_selector).text
            product_price = item.find_element(By.CSS_SELECTOR, price_selector).text
            # print(f'{item}')
            print(f'상품명: {product_name}, 가격: {product_price}')
        except:
            print(f'상품명: {product_name}, 판매중단')

driver = webdriver.Chrome()

search_product(driver)

infinite_scroll(driver)

AD_PRODUCT_SELECTOR = ".adProduct_item__1zC9h"
NONE_AD_PRODUCT_SELECTOR = ".product_item__MDtDF"

ad_product = driver.find_elements(By.CSS_SELECTOR, AD_PRODUCT_SELECTOR)
none_ad_product = driver.find_elements(By.CSS_SELECTOR, NONE_AD_PRODUCT_SELECTOR)

AD_PRODUCT_NAME_SELECTOR = ".adProduct_title__amInq"
NONE_AD_PRODUCT_NAME_SELECTOR = ".product_title__Mmw2K"
PRODUCT_PRICE_SELECTOR  = ".price_num__S2p_v"

print_ad_product(ad_product, AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)
print_ad_product(none_ad_product, NONE_AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)

# while(True):
#     next_page = input("다음 페이지 정보를 원하시면 'next'를 입력해주세요 (종료는 아무키나 입력해주세요.): ")
#     if next_page != 'next':
#         driver.quit()
#         break
#     else :
#         driver.find_element(By.CSS_SELECTOR, '.pagination_next__pZuC6').click()
#         infinite_scroll(driver)
    
#         ad_product = driver.find_elements(By.CSS_SELECTOR, AD_PRODUCT_SELECTOR)
#         none_ad_product = driver.find_elements(By.CSS_SELECTOR, NONE_AD_PRODUCT_SELECTOR)

#         print_ad_product(ad_product, AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)
#         print_ad_product(none_ad_product, NONE_AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)

# input()