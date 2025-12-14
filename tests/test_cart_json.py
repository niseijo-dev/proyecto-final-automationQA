import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_json_data

productos = load_json_data("productos.json")

@pytest.mark.ui
def test_verificar_productos_json(driver):
    login = LoginPage(driver)
    login.navegar()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    assert inv.obtener_titulo() == "Products"
    print(f"Validando contra {len(productos)} productos del JSON")