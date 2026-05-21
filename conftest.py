import pytest
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_user_csv

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options= options)
    
    #permite hacer una pausa e insertar el codigo que yo quiera
    yield driver 

    driver.quit()

#funcion de logueo global
@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    #llamo al csv y capturo el primer valor, el usuario correcto
    user = read_user_csv()[0]
    
    login_page.login(user["username"],user["password"])
    return driver
    
