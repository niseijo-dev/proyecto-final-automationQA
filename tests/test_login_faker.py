import pytest
from faker import Faker
from pages.login_page import LoginPage

fake = Faker()

@pytest.mark.ui
def test_login_usuario_random(driver):
    login = LoginPage(driver)
    login.navegar()
    login.login(fake.user_name(), fake.password())
    assert "Epic sadface" in login.obtener_error()