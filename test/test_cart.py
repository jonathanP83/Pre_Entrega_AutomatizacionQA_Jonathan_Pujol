from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke
def test_cart(driver_logged):
        # driver_logged ya realiza el login automaticamente
        driver = driver_logged
        
        #agretar producto al carrito
        driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

        #verificar contador
        
        contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
        
        assert contador_cart.text == "1", "el producto no se agrego correctamente"
        
        #obetener nombre del producto
        
        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
        
        #ir al carrito
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
        
        #verificar elemento agregado al carrito
        
        assert cart_item == product_name, "el producto agregado no coincide"