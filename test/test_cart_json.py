from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.inventory_page import InventoryPage
from page.cart_page import CartPage 
from utils.data_reader import read_products_json
from utils.logger import logger

def test_cart_json(driver_logged):
    inventory_page = InventoryPage (driver_logged)
    cart_page = CartPage(driver_logged)
    
    logger.info("Iniciando test_cart_json - cargando productos desde JSON")
    productos = read_products_json()
    
    logger.info(f"Agregando {len(productos)} productos al carrito")
    for producto in productos:
        #agregar el producto por nombre
        inventory_page.agregar_producto_por_nombre(producto["nombre"])
    
    #vamos al carrito    
    inventory_page.ir_al_carrito()
    logger.info("Navegando al carrito y validando productos")
    #obtengo los productos que estan en el carrito
    productos_carrito = cart_page.obtener_productos_carrito()
    
    #hago la validacion
    #si encuentra el producto lo deja en true, sino es false
    for producto_esperado in productos:
        encontrado = False
        #recorro los productos que tengo en el carrito
        for producto_json in productos_carrito:
            #hago un condicional para ver los productos que tengo en el carrito sean los mismos que tengo en el json
            if producto_json["nombre"] == producto_esperado["nombre"] and producto_json["precio"] == producto_esperado["precio"]:
                encontrado = True
                break
        assert encontrado, f"Producto Incorrecto o Faltante: {producto_esperado['nombre']}"
    
    
    
        
