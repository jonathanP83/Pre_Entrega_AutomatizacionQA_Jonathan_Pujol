from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage
# def test_login_validation(login_in_driver):
#     try:
#         driver = login_in_driver
#         #assert titulo
#         #assert productos en catalogo
#         #assert presencia de elementos
        

#         assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
#     except Exception as e:
#         print(f"Error en test_login: {e}")
#         raise

def test_inventory_title(driver_logged):
    inventory_page =InventoryPage(driver_logged)
    
    titulo = inventory_page.obtener_titulo()
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"

@pytest.mark.smoke
def test_productos_visibles(driver_logged):
    inventory_page =InventoryPage(driver_logged)
    
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0

def test_ui_elements(driver_logged):
    inventory_page =InventoryPage(driver_logged)
    
    assert inventory_page.menu_visible(), "El menu no está presente en la pagina"

    assert inventory_page.filtro_visible(), "El filtro no está presente en la pagina"

    