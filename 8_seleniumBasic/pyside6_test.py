import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_search import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

class searchWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(searchWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search_product)
        self.driver = webdriver.Chrome()
        self.textBrowser.setOpenExternalLinks(True)

    def search_product(self):
        self.textBrowser.clear()
        query = self.lineEdit.text()
        self.driver.get(f"https://search.shopping.naver.com/search/all?query={query}")
        self.driver.implicitly_wait(10)
        self.infinite_scroll()

        AD_PRODUCT_SELECTOR = ".adProduct_item__1zC9h"
        NONE_AD_PRODUCT_SELECTOR = ".product_item__MDtDF"

        ad_product = self.driver.find_elements(By.CSS_SELECTOR, AD_PRODUCT_SELECTOR)
        none_ad_product = self.driver.find_elements(By.CSS_SELECTOR, NONE_AD_PRODUCT_SELECTOR)

        AD_PRODUCT_NAME_SELECTOR = ".adProduct_title__amInq"
        NONE_AD_PRODUCT_NAME_SELECTOR = ".product_title__Mmw2K"
        PRODUCT_PRICE_SELECTOR  = ".price_num__S2p_v"

        self.print_ad_product(ad_product, AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)
        self.print_ad_product(none_ad_product, NONE_AD_PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR)

    def infinite_scroll(self):
        before_h = self.driver.execute_script("return window.scrollY")
        while True:
            self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            time.sleep(1)
            after_h = self.driver.execute_script("return window.scrollY")
            if before_h == after_h:
                break
            before_h = after_h
        time.sleep(5)

    def print_ad_product(self, items, name_selector, price_selector):
        for item in items:
            try:
                product_name = item.find_element(By.CSS_SELECTOR, name_selector).text
                product_price = item.find_element(By.CSS_SELECTOR, price_selector).text
                product_link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                # self.textBrowser.append(f'상품명:\n{product_name}\n')
                # self.textBrowser.append(f'가격: {product_price}\n')
                # self.textBrowser.append(f'링크: <a href="{product_link}">link</a>\n')
                self.textBrowser.append(
                f'상품명:<br>{product_name}<br><br>'
                f'가격: {product_price}<br>'
                f'링크: <a href="{product_link}">link</a><br>'
                '---------------------------------------------------------'
            )
            except:
                self.textBrowser.append(f'상품명:\n{product_name}\n\n')
                self.textBrowser.append(f'판매중단\n')
                self.textBrowser.append('---------------------------------------------------------')


app = QApplication(sys.argv)
window = searchWindow()
window.show()
app.exec_()
