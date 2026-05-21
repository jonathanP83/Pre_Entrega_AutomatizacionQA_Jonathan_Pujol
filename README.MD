# Proyecto de Automatización QA - Jonathan Pujol

## Descripción

Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest.

El objetivo del proyecto es automatizar pruebas E2E de distintas funcionalidades de una aplicación web de e-commerce (SauceDemo - https://www.saucedemo.com/).

## Tecnologías Usadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- CSV / JSON (data-driven testing)
- Git

## Instalación

```bash
git clone https://github.com/jonathanP83/Pre_Entrega_AutomatizacionQA_Jonathan_Pujol
```

## Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
Pre_Entrega_AutomatizacionQA_Jonathan_Pujol/
├── conftest.py            # Fixtures de pytest: driver Chrome + login automático
├── pytest.ini             # Configuración de pytest y generación de reportes HTML
├── requirements.txt       # Dependencias del proyecto
├── selectors.md           # Documentación de selectores CSS/ID de SauceDemo
├── page/                  # Page Objects
│   ├── login_page.py      # Page Object del login
│   ├── inventory_page.py  # Page Object del inventario
│   └── cart_page.py       # Page Object del carrito
├── utils/
│   └── data_reader.py     # Lectores de datos: CSV (usuarios) y JSON (productos)
├── data/
│   ├── users.csv          # Datos de usuarios para login
│   └── products.json      # Datos de productos esperados en el carrito
└── test/
    ├── test_login.py        # Validación de login exitoso
    ├── test_login_csv.py    # Login con datos parametrizados desde CSV
    ├── test_inventory.py    # Tests del inventario (título, productos, UI)
    ├── test_cart.py         # Test del carrito (agregar producto, contador, verificación)
    └── test_cart_json.py    # Test del carrito con datos parametrizados desde JSON
```

## Ejecución de Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar un test específico
pytest test/test_cart.py -v

# Ejecutar con reporte HTML
pytest --html=report.html --self-contained-html
```

Los reportes HTML se generan automáticamente gracias a la configuración en `pytest.ini`.

## Tests Incluidos

| Test | Descripción |
|------|-------------|
| `test_login_validation` | Verifica que el login redirige correctamente a `/inventory.html` |
| `test_login_csv` | Login parametrizado con múltiples usuarios desde CSV |
| `test_inventory_title` | Verifica que el título de la página es "Swag Labs" |
| `test_productos_visibles` | Verifica que hay productos visibles en el catálogo |
| `test_ui_elements` | Verifica que el menú hamburguesa y el filtro de productos están visibles |
| `test_cart` | Verifica el flujo completo: agregar producto al carrito, validar el contador y confirmar que el producto aparece en el carrito |
| `test_car_json` | Agrega múltiples productos desde JSON y valida que todos aparezcan correctamente en el carrito |

## Cómo Funciona

### Fixtures (conftest.py)

El archivo `conftest.py` define dos fixtures que se comparten entre todos los tests:

- **`driver`**: Inicia Chrome en modo incógnito y lo cierra automáticamente al finalizar cada test
- **`driver_logged`**: Usa el fixture `driver` y ejecuta el login automático antes de cada test usando datos de `data/users.csv`, evitando repetir código

### Page Objects (page/)

- **`login_page.py`**: Encapsula el flujo de autenticación (navegar, ingresar credenciales, clic en login)
- **`inventory_page.py`**: Métodos para obtener productos, verificar UI, agregar productos al carrito (por índice o por nombre), navegar al carrito
- **`cart_page.py`**: Obtiene la lista de productos en el carrito con su nombre y precio

### Data-Driven Testing (utils/data_reader.py)

- **`read_user_csv()`**: Lee `data/users.csv` y retorna una lista de diccionarios con las credenciales
- **`read_products_json()`**: Lee `data/products.json` y retorna una lista de productos esperados

### Flujo de Ejecución

Cada test recibe el driver ya logueado gracias al fixture `driver_logged`. Esto permite que los tests se enfoquen únicamente en la funcionalidad que están probando sin repetir pasos de autenticación.

## Notas

- El archivo `selectors.md` contiene todos los selectores CSS e IDs de SauceDemo como referencia
- Credenciales de prueba: `standard_user` / `secret_sauce`
- Se utiliza `find_elements` (plural) cuando se necesita acceder a una lista de elementos con índice `[0]`
- Se utiliza `find_element` (singular) cuando se busca un único elemento
- En los Page Objects, al iterar sobre una colección de WebElements, se usa `elemento.find_element(...)` para buscar dentro del contexto de ese elemento específico, no en toda la página
