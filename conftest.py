import pytest
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_user_csv
import pathlib
import pytest_html

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless=new")

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
    
#vamos a trabajar con un hook un gancho, permite ejecutar algo en determinados momentos
#esto ejecuta el codigo cuando termina cada test, se ejecuta el hook antes que otros, y hookwraper permite de cienta forma envolver el comportamiento

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
#defino la prueba en si, y me quedo con los dos parametros que me voy a quedar intermamente en la prueba
#el yield permite que se ejecute normalmente y vuelva a la linea yield
def pytest_runtest_makereport(item,call):
    outcome = yield
    
    #guardo en report el resultado de la prueba
    report = outcome.get_result()
    
    #when puede ser = setup, call o teardown
    if report.when == "call" and report.failed:
        #ahora capturo el driver, o sea la pantalla
        driver = item.funcargs.get("driver")
        
        #evaluo si hay driver o no
        if driver:
            #creo carpeta de las capturas de driver / screenshots
            target = pathlib.Path("reports/screenshots")
            #creo la carpeta, y si existe no la creo
            target.mkdir(parents=True,exist_ok=True)
            
            #defino nombre de archivo nombre prueba.png
            file_name = target / f"{item.name}.png"
            
            #ahora tomo la foto
            driver.save_screenshot(str(file_name))

            #esto es una evaluacion y fallaba por que estaba dentro del if lo demas
            #evaluo si el reporte soporte elementos extras
            if hasattr(report,"extra"):
                report.extra.append({
                    "name" : "screenshot",
                    "format" : "image",
                    "content" : str(file_name)
                })
            #le paso un atributo /lo obtengo y lo agrego a report que es extra
            extras = getattr(report,"extras",[])
            #lo adjuntamos al pytest_html
            extras.append(pytest_html.extras.png(str(file_name)))
            #guardo el extra en el reporte
            report.extras = extras
                
                                    
                                    
    