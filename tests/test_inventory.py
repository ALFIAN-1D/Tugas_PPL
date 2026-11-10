import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    def test_add_to_cart_flow(self, driver):
        # Kasus Uji 1: Tambahkan produk ke keranjang belanja
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        # Validasi badge keranjang belanja bernilai "1"
        assert inventory_page.get_cart_badge_count() == "1"

    def test_logout_flow(self, driver):
        # Kasus Uji 2: Logout dari aplikasi
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        # Validasi dialihkan ke URL utama dan tombol login kembali tampil
        assert login_page.get_current_url() == "https://www.saucedemo.com/"
        assert login_page.is_login_button_displayed() is True