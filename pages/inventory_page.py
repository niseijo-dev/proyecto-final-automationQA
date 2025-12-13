from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.title = (By.CLASS_NAME, "title")
        self.cart_btn = (By.CLASS_NAME, "shopping_cart_link")
        # Botones específicos para agregar productos
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def obtener_titulo(self):
        """Devuelve el título de la sección (ej: 'Products')"""
        return self.driver.find_element(*self.title).text

    def agregar_mochila(self):
        """Hace clic en 'Add to cart' de la mochila"""
        self.driver.find_element(*self.add_backpack).click()
        
    def ir_al_carrito(self):
        """Navega hacia el carrito de compras"""
        self.driver.find_element(*self.cart_btn).click()