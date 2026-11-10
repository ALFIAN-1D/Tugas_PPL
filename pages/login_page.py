from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object untuk halaman Login Saucedemo."""
    URL = "https://www.saucedemo.com/"

    # Elemen Lokator (Relative XPath)
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name' or @data-test='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password' or @data-test='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @id='login-button']")
    ERROR_CONTAINER = (By.XPATH, "//h3[@data-test='error' or contains(@class, 'error-message')]")
    APP_LOGO = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_CONTAINER)

    def is_dashboard_displayed(self) -> bool:
        return self.find_element(self.APP_LOGO).is_displayed()

    def is_login_button_displayed(self) -> bool:
        return self.find_element(self.LOGIN_BUTTON).is_displayed()