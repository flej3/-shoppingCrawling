import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

def find_rank():
    query = "python flask"
    search_link = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}"
    driver.get(search_link)
    time.sleep(2)

    target_blog_link = "https://cafe.naver.com/kstartupleaders/30396?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6ImtzdGFydHVwbGVhZGVycyIsImFydGljbGVJZCI6MzAzOTYsImlzc3VlZEF0IjoxNzA2Mzc0NjA3MTY2fQ.CbXpQ9sbTCybMgydsoCpnqXtk_D9sKg4udth2QmggeQ"
    link_selector = f'a[href^="{target_blog_link}"]'

    BLOG_FOUND = False
    for _ in range(7):
        try:
            element = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                curRank = new_element.get_attribute("data-cr-rank")
                if curRank is not None:
                    rank_label.config(text=f"{query}의 랭크는: {curRank} 입니다.")
                    BLOG_FOUND = True
                    break
                element = new_element
            if BLOG_FOUND:
                break
        except:
            driver.execute_script("window.scrollBy(0, 10000);")
            time.sleep(3)

    if not BLOG_FOUND:
        rank_label.config(text="타겟 블로그의 랭크를 찾지 못했습니다.")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

window = tk.Tk()
window.title("타겟 블로그 랭크 검색")
window.geometry("300x100")

find_button = tk.Button(window, text="Find Rank", command=find_rank)
find_button.pack()

rank_label = tk.Label(window, text="")
rank_label.pack()

window.mainloop()
