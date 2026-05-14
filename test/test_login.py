#ya no usamos mas selenium importamos directamente las cosas
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

#llamo a login page de page
from page.login_page import LoginPage

# funcion vieja
# def test_login_validation(login_in_driver):
#     try:
#         driver = login_in_driver

#         assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
#     except Exception as e:
#         print(f"Error en test_login: {e}")
#         raise

def test_login_ok(driver):
    #lo que estamos haciendo aca es crear un objeto, para poder usar los valores que estan dentro de la clase
    login_page = LoginPage(driver)

    #aca le paso los datos de ingreso al login
    login_page.login("standard_user","secret_sauce")

    #valido estar dentro del inventario
    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

#test para ver un caso erroneo
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","123456")
    
    #creo variable error, y traigo el resultado del error de login_page
    error = login_page.get_error_password_message()

    #valido el mensaje erroneo, de lo contrario el password esta bien
    assert "Epic sadface: Username and password do not match any user in this service"

    


