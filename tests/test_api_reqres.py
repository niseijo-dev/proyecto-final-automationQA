import pytest
import requests
from utils.logger import get_logger

log = get_logger()
BASE_URL = "https://reqres.in/api"

@pytest.mark.api
def test_get_users_list():
    log.info("API: Consultando lista de usuarios")
    res = requests.get(f"{BASE_URL}/users?page=2")
    assert res.status_code == 200
    assert len(res.json()['data']) > 0

@pytest.mark.api
def test_create_user_post():
    log.info("API: Creando nuevo usuario")
    res = requests.post(f"{BASE_URL}/users", json={"name": "Morpheus", "job": "Leader"})
    assert res.status_code == 201
    assert res.json()['name'] == "Morpheus"

@pytest.mark.api
def test_delete_user():
    log.info("API: Eliminando usuario")
    res = requests.delete(f"{BASE_URL}/users/2")
    assert res.status_code == 204