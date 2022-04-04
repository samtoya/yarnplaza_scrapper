from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from product import Product


class YarnPlaza:
    def __init__(self):
        self.uri = "https://www.yarnplaza.com/"
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.brands = ['https://www.yarnplaza.com/yarn/dmc',
                       'https://www.yarnplaza.com/yarn/drops',
                       'https://www.yarnplaza.com/yarn/stylecraft'
                       ]
        # self.browser.maximize_window()

    def start(self):
        try:
            self.browser.get(url=self.uri)
            WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.ID, "MasterBody"))
            )
            for brand in self.brands:
                self.browser.get(brand)
                WebDriverWait(self.browser, 10).until(
                    ec.presence_of_element_located((By.ID, "ContentPlaceHolder1_pnlFilterBarTop"))
                )
                elements = self.browser.find_elements(by=By.CLASS_NAME, value="productlist25")
                for element in elements:
                    title = element.find_element(by=By.CLASS_NAME, value="productlist-title").find_element(
                        by=By.TAG_NAME, value="a").text
                    price = element.find_element(by=By.CLASS_NAME, value="product-price-amount").text
                    image = element.find_element(by=By.CLASS_NAME, value="productlist-imgholder").find_element(
                        by=By.TAG_NAME, value="img").get_attribute("src")
                    currency = element.find_element(by=By.CLASS_NAME, value="product-price-currency").text
                    p = Product(title=title, price=price, currency=currency, image=image)
                    print(p.title)
                    print(p.price)
                    print(p.currency)
                    print(p.image)

                    # TODO: Handle pagination links
                    # pagination = self.browser.find_element(by=By.CLASS_NAME, value="paging-ul")

                    # Save each product in a csv or database.

        finally:
            self.browser.quit()


if __name__ == '__main__':
    y = YarnPlaza()
    y.start()
