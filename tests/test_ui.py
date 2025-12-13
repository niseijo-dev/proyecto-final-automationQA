import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_login_pom(driver):
    login = LoginPage(driver)
    login.navegar()
    # Datos fijos por ahora, cumpliendo solo con POM
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    assert "Products" in inv.obtener_titulo()