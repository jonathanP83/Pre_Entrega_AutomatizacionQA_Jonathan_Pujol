from behave import given, when, then
import requests

headers = {
    "x-api-key" : "pub_119a3c0639b47e5d4e32202f096674a01cad05389ba439ea2558977ace3dd0fa"
    
}
#scenario 1
@given("la API de Reqres esta disponible")
def step_acceder_api(context):
    context.base_url = "https://reqres.in/api"

@when("realizar un login valido")
def step_login(context):
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json=body
    )
#convertir a entero con :d o  :f si es decimal
@then("el status code debe ser {status_code:d}")
def step_validation_status(context, status_code):
    assert context.response.status_code == status_code

#scenario 2
@when("realizar un login sin contraseña")
def step_login_sin_password(context):
    body = {
        "email": "eve.holt@reqres.in",
    }
    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json=body
    )

@then("el mensaje de error debe ser '{mensaje}'")
def step_validar_error(context, mensaje):
    body = context.response.json()

    assert body["error"] == mensaje



                        
                        