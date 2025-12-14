import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_csv_data
from utils.logger import get_logger

log = get_logger()
datos = load_csv_data("login.csv")

@pytest.mark.ui
@pytest.mark.smoke
def test_login_standard_user(driver):
    log.info("Inicio Test: Login Standard User")
    login = LoginPage(driver)
    login.navegar()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    assert "Products" in inv.obtener_titulo()
    log.info("Fin Test: Login exitoso")

@pytest.mark.ui
@pytest.mark.parametrize("u,c,r", [(d['usuario'], d['clave'], d['resultado_esperado']) for d in datos])
def test_login_data_driven(driver, u, c, r):
    log.info(f"Inicio Test Data-Driven: Usuario {u}")
    login = LoginPage(driver)
    login.navegar()
    login.login(u, c)
    if r == "success":
        assert "Products" in InventoryPage(driver).obtener_titulo()
    else:
        assert "Epic sadface" in login.obtener_error()
    log.info("Fin Test Data-Driven")