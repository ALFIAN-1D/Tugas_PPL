from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Lokator Relative XPath yang tangguh dan tanpa Absolute XPath
    ADD_BACKPACK_BTN = (By.XPATH, "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]")
    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    BURGER_MENU_BTN = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def get_cart_badge_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def logout(self):
        self.click(self.BURGER_MENU_BTN)
        self.click(self.LOGOUT_LINK)