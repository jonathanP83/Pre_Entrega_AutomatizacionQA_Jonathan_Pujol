from page.login_page import LoginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke
def test_login_ok(driver):
    
    #agrego los logger en cada seccion de las pruebas
    
    logger.info("inicializando el driver para test login_ok")
    #lo que estamos haciendo aca es crear un objeto, para poder usar los valores que estan dentro de la clase
    login_page = LoginPage(driver)
    
    logger.info("inicialidanzo los datos de entrada para la prueba")
    
    #aca le paso los datos de ingreso al login
    login_page.login("standard_user","secret_sauce")

    logger.info("iniciando sesion...")
    #valido estar dentro del inventario
    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    logger.info("sesion iniciada correctamente")

#test para ver un caso erroneo
def test_login_invalid_password(driver):
    logger.info("inicializando el driver para test login_invalid_password")
    login_page = LoginPage(driver)

    logger.info("ingresando credenciales invalidas")
    login_page.login("standard_user","123456")
    
    #creo variable error, y traigo el resultado del error de login_page
    logger.info("obteniendo mensaje de error")
    error = login_page.get_error_message()

    #valido el mensaje erroneo, de lo contrario el password esta bien
    assert "Epic sadface: Username and password do not match any user in this service" in error
    logger.info("validando mensaje de error")
    logger.info("validacion completada")

    


