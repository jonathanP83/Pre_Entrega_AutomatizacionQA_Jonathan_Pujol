from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
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

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver


def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "el titulo de la pagina que se accese no es correcto"


def test_productos_visibles(driver_logged):
    productos_visibles = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos_visibles) > 0 
    
def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filtro= driver_logged.find_element(By.CLASS_NAME,"product_sort_container")

    assert menu.is_displayed()
    assert filtro.is_displayed()


