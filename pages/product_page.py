from selenium.common.exceptions import NoAlertPresentException
import math

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def assert_product_name(self):
        product_name_should_be = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_PRODUCT).text
        assert product_name == product_name_should_be,\
            f"Product in basket: {product_name}, should be: {product_name_should_be}"

    def assert_basket_total(self):
        product_price_should_be = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        basket_amount = total.split()
        assert basket_amount[2] == product_price_should_be,\
            f"Basket total: {basket_amount[2]} should be: {product_price_should_be}"