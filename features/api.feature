@api
Feature: Login API Reqres

    Scenario: Login valido
        Given la API de Reqres esta disponible
        When realizar un login valido
        Then el status code debe ser 200

    Scenario: login sin password
        Given la API de Reqres esta disponible
        When realizar un login sin contraseña
        Then el status code debe ser 400
        And el mensaje de error debe ser 'Missing password'
