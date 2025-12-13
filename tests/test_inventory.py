import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_verificar_titulo_inventario(driver):
    login = LoginPage(driver)
    login.navegar()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    assert inv.obtener_titulo() == "Products"