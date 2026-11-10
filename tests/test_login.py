import pytest
from pages.login_page import LoginPage


class TestLogin:
    def test_login_positive_valid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        expected_inventory_url = "https://www.saucedemo.com/inventory.html"
        assert login_page.get_current_url() == expected_inventory_url
        assert login_page.is_dashboard_displayed() is True

    def test_login_negative_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        assert expected_error in login_page.get_error_message()

    def test_login_negative_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "")

        expected_error = "Epic sadface: Password is required"
        assert expected_error in login_page.get_error_message()