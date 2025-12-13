import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
@pytest.mark.smoke
def test_login_standard_user(driver):
    login = LoginPage(driver)
    login.navegar()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    assert "Products" in inv.obtener_titulo()