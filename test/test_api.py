import requests

#en la variable headers dedino los metadatos

headers = {
    "x-api-key" : "pub_119a3c0639b47e5d4e32202f096674a01cad05389ba439ea2558977ace3dd0fa"
    
}

#diccionario
# body = {
    
#     "name" : "jonathan",
#     "job" : "tester QA"
# }

#get pido dato uso headers
#post mando dato uso body
#delete borro dato no uso body
#put actualiza por completo el dato
#patch modifico dato parcialmente uso body
#capturo los datos de la llamada a la api en la variable response, y le paso al encabezado la variable headers, que es la clave la api key
#response = requests.patch("https://reqres.in/api/users/2", headers=headers,json=body)

#hago un print de los datos, que viajan en un json y imprimo el status code
#print(response.status_code)
#print(response.json())

def test_login_valido():
    #creamos body con usuario y contraseña valido
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    #llamamos a la api, pasamos headers metadatos y json body
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    #hacemos la validacion si da 200 esta correcto
    assert response.status_code == 200

def test_login_sin_password():    

    #creamos body con usuario y SIN contraseña
    body = {
        "email": "eve.holt@reqres.in",

    }
    #llamamos a la api, pasamos headers metadatos y json body
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    #hacemos la validacion si da 400 esta correcto por que no tiene la contraseña
    assert response.status_code == 400

def test_create_user():
    #creo usuario
    body = {
        "name": "jonathan",
        "email": "jonathan@hotmail.com",
        "password": "123456"
        
    }
    #se lo paso a la api
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    
     #almaceno la informacion que me da la respuesta la api , guardo en formato json lo que me respondio la api
    data = response.json()
    
    
    assert response.status_code == 201
    #valido los datos que estan en data , si quiero verlos tiro un print son -s al correr el test
    
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]
    #valido tiempo de respuesta que toma hacer la respuesta
    assert response.elapsed.total_seconds() < 1

#test de eliminar el usuario, aca en el url voy a users, ejemplo le damos el 2    
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2",headers=headers)

#verificamos con 204 que se borro
    assert response.status_code == 204

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2",headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"