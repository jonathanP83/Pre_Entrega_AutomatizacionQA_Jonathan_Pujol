from selenium.webdriver.common.by import By

#esto es para que si cambia algo en la pagina, no tener que re hacer todo, sino modificar aca los valores puntuales, y todo seguiria funcionando, es para pode escalar
class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        #llamo a todos los selectores
        self.username_input = (By.ID,"user-name")
        self.password_input =(By.ID,"password")
        self.login_button =(By.ID,"login-button")
        #en vez de by, uso css y busco el elemento que tiene de atributo error
        self.error_password =(By.CSS_SELECTOR, "[data-test='error']")

    #funcion de abrir la pagina
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    #creo funciones de interaccion
    #uso puntero, que guarda un valor, del valor que esta en memoria (la direccion de la caja)
    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


    #en esta funcion se llama a todas las funciones con los paramentros que yo quiera

    def login(self,usuario,password):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    #funcion captura error
    def get_error_password_message(self):
        error =self.driver.find_element(*self.error_password).text 
        print(error)
        return error


