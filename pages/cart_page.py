from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.checkout_btn = (By.ID, "checkout")
        self.cart_item = (By.CLASS_NAME, "cart_item")

    def hay_productos(self):
        """Devuelve True si hay al menos un producto en el carrito"""
        items = self.driver.find_elements(*self.cart_item)
        return len(items) > 0