import pytest
from selenium import webdriver

#from utils.LoginPage import login

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options= options)

    yield driver

    driver.quit()


# se borro comento para no perder, no lo usamos por que llamamos a driver en conftest
# @pytest.fixture
# def login_in_driver(driver):
#     login(driver)
#     return driver