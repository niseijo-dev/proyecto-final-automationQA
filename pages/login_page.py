from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    
    def __init__(self, driver):
        self.driver = driver
        # Locators (Selectores)
        self.user_input = (By.ID, "user-name")
        self.pass_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "[data-test='error']")

    def navegar(self):
        """Abre la página de login"""
        self.driver.get(self.URL)

    def login(self, usuario, clave):
        """Realiza el proceso de login completo"""
        self.driver.find_element(*self.user_input).send_keys(usuario)
        self.driver.find_element(*self.pass_input).send_keys(clave)
        self.driver.find_element(*self.login_btn).click()

    def obtener_error(self):
        """Devuelve el texto del mensaje de error si existe"""
        return self.driver.find_element(*self.error_msg).text