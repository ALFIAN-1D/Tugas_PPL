import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestInventory:
    def test_add_to_cart_flow(self, driver):
        # Kasus Uji 1: Login dan tambahkan produk ke keranjang
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        # Assertion: Validasi badge keranjang belanja menunjukkan teks "1"
        expected_count = "1"
        actual_count = inventory_page.get_cart_badge_count()
        assert actual_count == expected_count, (
            f"Gagal: Diharapkan badge angka '{expected_count}', Diterima: '{actual_count}'"
        )

    def test_logout_flow(self, driver):
        # Kasus Uji 2: Login lalu lakukan proses logout
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        # PENTING: Kita pancing Explicit Wait dengan mencari tombol login terlebih dahulu.
        # Robot akan menunggu maksimal 10 detik sampai tombol ini selesai dirender.
        is_login_btn_visible = login_page.find_element(login_page.LOGIN_BUTTON).is_displayed()

        # Assertion 1: Buktikan tombol login kembali tampil
        assert is_login_btn_visible is True, "Gagal: Tombol login tidak tampil setelah proses logout."

        # Assertion 2: Setelah tombol login dipastikan ada, baru buktikan URL-nya berubah
        expected_login_url = "https://www.saucedemo.com/"
        actual_url = login_page.get_current_url()
        assert actual_url == expected_login_url, (
            f"Gagal: Diharapkan URL '{expected_login_url}', aktual '{actual_url}'"
        )