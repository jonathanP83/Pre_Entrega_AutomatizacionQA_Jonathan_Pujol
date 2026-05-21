#ya no usamos mas selenium importamos directamente las cosas
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

#llamo a login page de page
from page.login_page import LoginPage
from utils.data_reader import read_user_csv
import pytest

#parametrizo, ejecuto una prueba con un dato, va de coleccion de datos en coleccion de datos
#capturo usuario, que la funcion viene de read_user_csv
@pytest.mark.parametrize("user", read_user_csv())
def test_login(driver, user):
    login_page =LoginPage(driver)
    #llamo al elemento que me trae esa funciona traves de la clave, o sea llamo los usuarios y contraseñas
    #desde el diccionario de user
    login_page.login(user["username"],user["password"])
    if user["valid"]== "true":
        assert "/inventory.html" in driver.current_url, "no se redirigio al invventario"
    else:
        #capturo el mensaje de error y valido si el error de login contiene en su mensaje "Epic sadface"
        error = login_page.get_error_password_message()    
        assert "Epic sadface" in error



