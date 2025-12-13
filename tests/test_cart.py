import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_agregar_item_carrito(driver):
    login = LoginPage(driver)
    login.navegar()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.agregar_mochila()
    inv.ir_al_carrito()
    cart = CartPage(driver)
    assert cart.hay_productos() is True