# Proyecto de Automatización QA - Jonathan Pujol

## Descripción

Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest.

El objetivo del proyecto es automatizar pruebas E2E de distintas funcionalidades de una aplicación web de e-commerce (SauceDemo - https://www.saucedemo.com/).

## Tecnologias Usadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git

## Instalacion

```bash
git clone https://github.com/jonathanP83/Pre_Entrega_AutomatizacionQA_Jonathan_Pujol
```

## intalación Dependencias (requerimientos)

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
Pre_Entrega_AutomatizacionQA_Jonathan_Pujol/
├── conftest.py            # Fixtures de pytest: driver Chrome + login automático
├── pytest.ini             # Configuración de pytest y generación de reportes HTML
├── requirements.txt       # Dependencias del proyecto
├── selectors.md           # Documentación de selectores CSS/ID de SauceDemo
├── utils/
│   └── LoginPage.py         # Page Object con la función de login
└── test/
    ├── test_login.py        # Validación de login exitoso
    ├── test_inventory.py    # Tests del inventario (título, productos, UI)
    └── test_cart.py         # Test del carrito (agregar producto, contador, verificación)
```

## Ejecución de tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar un test específico
pytest test/test_cart.py -v

# Ejecutar con reporte HTML
pytest --html=report.html --self-contained-html
```

Los reportes HTML se generan automáticamente gracias a la configuración en `pytest.ini`.

## Tests incluidos

| Test | Descripción |
|------|-------------|
| `test_login_validation` | Verifica que el login redirige correctamente a `/inventory.html` |
| `test_inventory_title` | Verifica que el título de la página es "Swag Labs" |
| `test_productos_visibles` | Verifica que hay productos visibles en el catálogo |
| `test_ui_elements` | Verifica que el menú hamburguesa y el filtro de productos están visibles |
| `test_cart` | Verifica el flujo completo: agregar producto al carrito, validar el contador y confirmar que el producto aparece en el carrito |

## Cómo funciona

### Fixtures (conftest.py)

El archivo `conftest.py` define dos fixtures que se comparten entre todos los tests:

- **`driver`**: Inicia Chrome en modo incógnito y lo cierra automáticamente al finalizar cada test
- **`login_in_driver`**: Usa el fixture `driver` y ejecuta el login automático antes de cada test, evitando repetir código

### Page Object (utils/LoginPage.py)

La función `login()` encapsula el flujo de autenticación:
1. Navega a `https://www.saucedemo.com/`
2. Ingresa usuario: `standard_user`
3. Ingresa contraseña: `secret_sauce`
4. Hace clic en el botón de login

### Flujo de ejecución

Cada test recibe el driver ya logueado gracias al fixture `login_in_driver`. Esto permite que los tests se enfoquen únicamente en la funcionalidad que están probando sin repetir pasos de autenticación.

## Notas

- El archivo `selectors.md` contiene todos los selectores CSS e IDs de SauceDemo como referencia
- Credenciales de prueba: `standard_user` / `secret_sauce`
- Se utiliza `find_elements` (plural) cuando se necesita acceder a una lista de elementos con índice `[0]`
- Se utiliza `find_element` (singular) cuando se busca un único elemento
