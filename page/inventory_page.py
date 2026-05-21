from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.filtro = (By.CLASS_NAME,"product_sort_container")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
    
    def obtener_titulo(self):
        return self.driver.title
    
    def obtener_productos(self):
        return self.driver.find_elements(*self.inventory_items)
    
    def menu_visible(self):
        return self.driver.find_element(*self.menu_button).is_displayed()
    
    def filtro_visible(self):
        return self.driver.find_element(*self.filtro).is_displayed()
    
    def agregar_producto_al_carrito(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.contador_carrito).text
    
    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.nombres_productos)[0].text
    
    def ir_al_carrito(self):
        self.driver.find_element(*self.link_carrito).click()
    
    #creo funcion que me permite agregar producto por nombre
    def agregar_producto_por_nombre(self,nombre_producto_json):
        #busco a inventory_items, guardo coleccion de todos los productos, y busco puntualmente el que quiero
        productos = self.driver.find_elements(*self.inventory_items)
        #recorro los productos para poder buscar cual necesito
        for producto in productos:
            nombre = producto.find_element(*self.nombres_productos).text
            
            #evaluo si nombre es el mismo que tengo en la base el jason
            #si es correcto, lo agrego al carrito
            if nombre == nombre_producto_json:
                producto.find_element(*self.add_to_cart_buttons).click()
                
                
        


